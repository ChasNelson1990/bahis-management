from rest_framework import permissions, viewsets

from bahis_management.desk_modules.models import DeskModule, DeskModuleType
from bahis_management.desk_modules.api.serializers import DeskModuleSerializer, DeskModuleTypeSerializer


class DeskModuleTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DeskModuleTypes to be viewed or edited.
    """

    queryset = DeskModuleType.objects.all().order_by("id")
    serializer_class = DeskModuleTypeSerializer
    permission_classes = [permissions.AllowAny]  # [permissions.IsAuthenticated] FIXME auth is turned off


class DeskModulesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DeskModules to be viewed or edited.
    """

    queryset = DeskModule.objects.all().order_by("parent_module_id", "sort_order")
    serializer_class = DeskModuleSerializer
    permission_classes = [permissions.AllowAny]  # [permissions.IsAuthenticated] FIXME auth is turned off
