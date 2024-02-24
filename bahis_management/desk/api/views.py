from bahis_management.desk.api.serializers import (
    ListDefinitionSerializer,
    ModuleSerializer,
    ModuleTypeSerializer,
    WorkflowSerializer,
)
from bahis_management.desk.models import (
    Module,
    ListDefinition,
    ModuleType,
    Workflow,
)
from rest_framework import permissions, viewsets


class ModuleTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ModuleTypes to be viewed or edited.
    """

    queryset = ModuleType.objects.all().order_by("id")
    serializer_class = ModuleTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # [permissions.IsAuthenticated] FIXME auth is turned off


class ListDefinitionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ListDefinitions to be viewed or edited.
    """

    queryset = ListDefinition.objects.all().order_by("id")
    serializer_class = ListDefinitionSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # [permissions.IsAuthenticated] FIXME auth is turned off


class ModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Modules to be viewed or edited.
    """

    queryset = Module.objects.all().order_by("parent_module", "sort_order")
    serializer_class = ModuleSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # [permissions.IsAuthenticated] FIXME auth is turned off


class WorkflowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Workflows to be viewed or edited.
    """

    queryset = Workflow.objects.all().order_by("id")
    serializer_class = WorkflowSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # [permissions.IsAuthenticated] FIXME auth is turned off
