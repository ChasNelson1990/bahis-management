from bahis_management.desk.models import (
    Module,
    ModuleListDefinition,
    ModuleWorkflow,
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


class ModuleListDefinitionList(FilterView):
    template_name_suffix = "_list"
    model = ModuleListDefinition
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


class ModuleListDefinitionCreate(CreateView):
    template_name_suffix = "_create_form"
    model = ModuleListDefinition
    fields = desk_module_list_definition_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(
            self.request, "The module list definition was created successfully."
        )
        return super(ModuleListDefinitionCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "The module list definition was not created successfully."
        )
        form.error_css_class = "error"
        return super(ModuleListDefinitionCreate, self).form_invalid(form)


class ModuleListDefinitionUpdate(UpdateView):
    template_name_suffix = "_update_form"
    model = ModuleListDefinition
    fields = desk_module_list_definition_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(
            self.request, "The module list definition was updated successfully."
        )
        return super(ModuleListDefinitionUpdate, self).form_valid(form)


class ModuleListDefinitionDelete(DeleteView):
    template_name_suffix = "_delete_form"
    model = ModuleListDefinition
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(
            self.request, "The module list definition was deleted successfully."
        )
        return super(ModuleListDefinitionDelete, self).form_valid(form)


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


class ModuleList(FilterView):
    template_name_suffix = "_list"
    model = Module
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


class ModuleCreate(CreateView):
    template_name_suffix = "_create_form"
    model = Module
    fields = desk_module_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(self.request, "The module was created successfully.")
        return super(ModuleCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "The module was not created successfully.")
        form.error_css_class = "error"
        return super(ModuleCreate, self).form_invalid(form)


class ModuleUpdate(UpdateView):
    template_name_suffix = "_update_form"
    model = Module
    fields = desk_module_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(self.request, "The module was updated successfully.")
        return super(ModuleUpdate, self).form_valid(form)


class ModuleDelete(DeleteView):
    template_name_suffix = "_delete_form"
    model = Module
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(self.request, "The module was deleted successfully.")
        return super(ModuleDelete, self).form_valid(form)


desk_module_workflow_entry_fields = [
    "title",
    "list_id",
    "form_id",
    "workflow_definition",
    "is_active",
]


class ModuleWorkflowList(FilterView):
    template_name_suffix = "_list"
    model = ModuleWorkflow
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


class ModuleWorkflowCreate(CreateView):
    template_name_suffix = "_create_form"
    model = ModuleWorkflow
    fields = desk_module_workflow_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(self.request, "The module workflow was created successfully.")
        return super(ModuleWorkflowCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "The module workflow was not created successfully."
        )
        form.error_css_class = "error"
        return super(ModuleWorkflowCreate, self).form_invalid(form)


class ModuleWorkflowUpdate(UpdateView):
    template_name_suffix = "_update_form"
    model = ModuleWorkflow
    fields = desk_module_workflow_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(self.request, "The module workflow was updated successfully.")
        return super(ModuleWorkflowUpdate, self).form_valid(form)


class ModuleWorkflowDelete(DeleteView):
    template_name_suffix = "_delete_form"
    model = ModuleWorkflow
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(self.request, "The module workflow was deleted successfully.")
        return super(ModuleWorkflowDelete, self).form_valid(form)
