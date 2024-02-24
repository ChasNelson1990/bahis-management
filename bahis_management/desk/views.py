from bahis_management.desk.models import (
    Module,
    ListDefinition,
    Workflow,
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


class ListDefinitionList(FilterView):
    template_name_suffix = "_list"
    model = ListDefinition
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


class ListDefinitionCreate(CreateView):
    template_name_suffix = "_create_form"
    model = ListDefinition
    fields = desk_module_list_definition_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(
            self.request, "The module list definition was created successfully."
        )
        return super(ListDefinitionCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "The module list definition was not created successfully."
        )
        form.error_css_class = "error"
        return super(ListDefinitionCreate, self).form_invalid(form)


class ListDefinitionUpdate(UpdateView):
    template_name_suffix = "_update_form"
    model = ListDefinition
    fields = desk_module_list_definition_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(
            self.request, "The module list definition was updated successfully."
        )
        return super(ListDefinitionUpdate, self).form_valid(form)


class ListDefinitionDelete(DeleteView):
    template_name_suffix = "_delete_form"
    model = ListDefinition
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(
            self.request, "The module list definition was deleted successfully."
        )
        return super(ListDefinitionDelete, self).form_valid(form)


desk_module_entry_fields = [
    "title",
    "icon",
    "description",
    "list_definition",
    "form_id",
    "external_url",
    "module_type",
    "parent_module",
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
        "parent_module": ["exact"],
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.list_definition:
            context["list_definition"] = self.object.list_definition.id

        return context


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


class WorkflowList(FilterView):
    template_name_suffix = "_list"
    model = Workflow
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


class WorkflowCreate(CreateView):
    template_name_suffix = "_create_form"
    model = Workflow
    fields = desk_module_workflow_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(self.request, "The module workflow was created successfully.")
        return super(WorkflowCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "The module workflow was not created successfully."
        )
        form.error_css_class = "error"
        return super(WorkflowCreate, self).form_invalid(form)


class WorkflowUpdate(UpdateView):
    template_name_suffix = "_update_form"
    model = Workflow
    fields = desk_module_workflow_entry_fields
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(self.request, "The module workflow was updated successfully.")
        return super(WorkflowUpdate, self).form_valid(form)


class WorkflowDelete(DeleteView):
    template_name_suffix = "_delete_form"
    model = Workflow
    success_url = reverse_lazy("desk:list")

    def form_valid(self, form):
        messages.success(self.request, "The module workflow was deleted successfully.")
        return super(WorkflowDelete, self).form_valid(form)
