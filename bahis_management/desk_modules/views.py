from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django_filters.views import FilterView
from bahis_management.desk_modules.models import DeskModule

desk_module_entry_fields = [
    "title",
    "icon",
    "description",
    "list_definition_id",
    "form_id",
    "external_url",
    "module_type",
    "parent_module_id",
    "sort_order",
    "is_active",
]


class DeskModuleList(FilterView):
    template_name_suffix = "_list"
    model = DeskModule
    paginate_by = 5
    ordering = ["id"]
    filterset_fields = {
        "title": ["icontains"],
        "description": ["icontains"],
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = dict()
        # remove page from query tag so pagination works in template
        for k, v in context["filter"].data.items():
            if k != "page":
                context["query"][k] = v

        # use paginator range with ellipses for simplicity
        page = context["page_obj"]
        context["paginator_range"] = page.paginator.get_elided_page_range(page.number, on_each_side=2, on_ends=2)

        return context


class DeskModuleCreate(CreateView):
    template_name_suffix = "_create_form"
    model = DeskModule
    fields = desk_module_entry_fields
    success_url = reverse_lazy("desk_modules:list")

    def form_valid(self, form):
        messages.success(self.request, "The module was created successfully.")
        return super(DeskModuleCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "The module was not created successfully.")
        form.error_css_class = "error"
        return super(DeskModuleCreate, self).form_invalid(form)


class DeskModuleUpdate(UpdateView):
    template_name_suffix = "_update_form"
    model = DeskModule
    fields = desk_module_entry_fields
    success_url = reverse_lazy("desk_modules:list")

    def form_valid(self, form):
        messages.success(self.request, "The module was updated successfully.")
        return super(DeskModuleUpdate, self).form_valid(form)


class DeskModuleDelete(DeleteView):
    template_name_suffix = "_delete_form"
    model = DeskModule
    success_url = reverse_lazy("desk_modules:list")

    def form_valid(self, form):
        messages.success(self.request, "The module was deleted successfully.")
        return super(DeskModuleDelete, self).form_valid(form)
