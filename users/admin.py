from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.utils.safestring import mark_safe

from bahis_management.desk.models import Module
from users.models import Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_groups')

    def get_groups(self, obj):
        return ", ".join([g.name for g in obj.groups.all()])

    get_groups.short_description = 'Groups'  # Label for the 'Groups' column


class CustomGroupAdmin(GroupAdmin):
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

    class Media:
        css = {
            'all': ('css/my_admin.css',)
        }


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)

# Register your models here.
admin.site.register(Module)
admin.site.register(Profile)
