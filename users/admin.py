from django import forms
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.utils.safestring import mark_safe

from bahis_management.desk.models import Module
from users.models import Profile


class GroupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance']:
            # Pre-populate the users field with existing users in the group
            self.fields['users'].initial = kwargs['instance'].user_set.all()

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'user-checkboxes'}),
        required=False,
        label="Select Users"
    )

    class Meta:
        model = Group
        fields = ['name', 'users']  # Include the fields you want to display


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_groups')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    list_per_page = 30
    search_fields = ('username', 'email', 'first_name', 'last_name')

    def get_groups(self, obj):
        return ", ".join([g.name for g in obj.groups.all()])

    get_groups.short_description = 'Groups'  # Label for the 'Groups' column


class GroupAdmin(admin.ModelAdmin):
    form = GroupForm
    list_display = ('name', 'get_users')

    def get_users(self, obj):
        users = obj.user_set.all()
        if users:
            # Adding an input search field
            search_input = '<input type="text" id="searchUser" placeholder="Search users..." onkeyup="filterUsers()">'
            user_list = ''.join(
                f'<div class="user-item"><a href="{reverse("admin:auth_user_change", args=[user.id])}">{user.username}</a></div>'
                for user in users
            )

            return mark_safe(f'''
                {search_input}
                <div class="user-list">{user_list}</div>
                <script>
                    function filterUsers() {{
                        let input = document.getElementById("searchUser");
                        let filter = input.value.toLowerCase();
                        let userItems = document.getElementsByClassName("user-item");
                        for (let i = 0; i < userItems.length; i++) {{
                            let userItem = userItems[i];
                            let username = userItem.innerText.toLowerCase();
                            if (username.includes(filter)) {{
                                userItem.style.display = "";
                            }} else {{
                                userItem.style.display = "none";
                            }}
                        }}
                    }}
                </script>
            ''')
        return "No users"

    get_users.short_description = 'Users'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if form.cleaned_data.get('users'):
            obj.user_set.set(form.cleaned_data['users'])  # Assign selected users to the group

    class Media:
        css = {
            'all': ('css/my_admin.css',)
        }
        js = ('js/my_admin.js',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

admin.site.register(Module)
admin.site.register(Profile)
