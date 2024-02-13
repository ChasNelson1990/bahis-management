from bahis_management.desk_modules.models import (
    DeskModule,
    DeskModuleListDefinition,
    DeskModuleWorkflow,
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView

desk_module_list_definition_entry_fields = [
    "title",
    "form_id",
    "column_definitions",
    "filter_definitions",
]


class DeskModuleListDefinitionList(FilterView):
    template_name_suffix = "_list"
    model = DeskModuleListDefinition
    paginate_by = 5
    ordering = ["id"]
    filterset_fields = {
        "title": ["icontains"],
        "form_id": ["exact"],
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
        context["paginator_range"] = page.paginator.get_elided_page_range(
            page.number, on_each_side=2, on_ends=2
        )

        return context


class DeskModuleListDefinitionCreate(CreateView):
    template_name_suffix = "_create_form"
    model = DeskModuleListDefinition
    fields = desk_module_list_definition_entry_fields
    success_url = reverse_lazy("desk_modules:list")

    def form_valid(self, form):
        messages.success(
            self.request, "The module list definition was created successfully."
        )
        return super(DeskModuleListDefinitionCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "The module list definition was not created successfully."
        )
        form.error_css_class = "error"
        return super(DeskModuleListDefinitionCreate, self).form_invalid(form)


class DeskModuleListDefinitionUpdate(UpdateView):
    template_name_suffix = "_update_form"
    model = DeskModuleListDefinition
    fields = desk_module_list_definition_entry_fields
    success_url = reverse_lazy("desk_modules:list")

    def form_valid(self, form):
        messages.success(
            self.request, "The module list definition was updated successfully."
        )
        return super(DeskModuleListDefinitionUpdate, self).form_valid(form)


class DeskModuleListDefinitionDelete(DeleteView):
    template_name_suffix = "_delete_form"
    model = DeskModuleListDefinition
    success_url = reverse_lazy("desk_modules:list")

    def form_valid(self, form):
        messages.success(
            self.request, "The module list definition was deleted successfully."
        )
        return super(DeskModuleListDefinitionDelete, self).form_valid(form)


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
        context["paginator_range"] = page.paginator.get_elided_page_range(
            page.number, on_each_side=2, on_ends=2
        )

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


desk_module_workflow_entry_fields = [
    "title",
    "list_id",
    "form_id",
    "workflow_definition",
    "is_active",
]


class DeskModuleWorkflowList(FilterView):
    template_name_suffix = "_list"
    model = DeskModuleWorkflow
    paginate_by = 5
    ordering = ["id"]
    filterset_fields = {
        "title": ["icontains"],
        "workflow_definition": ["icontains"],
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
        context["paginator_range"] = page.paginator.get_elided_page_range(
            page.number, on_each_side=2, on_ends=2
        )

        return context


class DeskModuleWorkflowCreate(CreateView):
    template_name_suffix = "_create_form"
    model = DeskModuleWorkflow
    fields = desk_module_workflow_entry_fields
    success_url = reverse_lazy("desk_modules:list")

    def form_valid(self, form):
        messages.success(self.request, "The module workflow was created successfully.")
        return super(DeskModuleWorkflowCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "The module workflow was not created successfully."
        )
        form.error_css_class = "error"
        return super(DeskModuleWorkflowCreate, self).form_invalid(form)


class DeskModuleWorkflowUpdate(UpdateView):
    template_name_suffix = "_update_form"
    model = DeskModuleWorkflow
    fields = desk_module_workflow_entry_fields
    success_url = reverse_lazy("desk_modules:list")

    def form_valid(self, form):
        messages.success(self.request, "The module workflow was updated successfully.")
        return super(DeskModuleWorkflowUpdate, self).form_valid(form)


class DeskModuleWorkflowDelete(DeleteView):
    template_name_suffix = "_delete_form"
    model = DeskModuleWorkflow
    success_url = reverse_lazy("desk_modules:list")

    def form_valid(self, form):
        messages.success(self.request, "The module workflow was deleted successfully.")
        return super(DeskModuleWorkflowDelete, self).form_valid(form)
