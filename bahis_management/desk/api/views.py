from bahis_management.desk.api.serializers import (
    ModuleListDefinitionSerializer,
    ModuleSerializer,
    ModuleTypeSerializer,
    ModuleWorkflowSerializer,
)
from bahis_management.desk.models import (
    Module,
    ModuleListDefinition,
    ModuleType,
    ModuleWorkflow,
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


class ModuleListDefinitionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ModuleListDefinitions to be viewed or edited.
    """

    queryset = ModuleListDefinition.objects.all().order_by("id")
    serializer_class = ModuleListDefinitionSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # [permissions.IsAuthenticated] FIXME auth is turned off


class ModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Modules to be viewed or edited.
    """

    queryset = Module.objects.all().order_by("parent_module_id", "sort_order")
    serializer_class = ModuleSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # [permissions.IsAuthenticated] FIXME auth is turned off


class ModuleWorkflowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ModuleWorkflows to be viewed or edited.
    """

    queryset = ModuleWorkflow.objects.all().order_by("id")
    serializer_class = ModuleWorkflowSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # [permissions.IsAuthenticated] FIXME auth is turned off
