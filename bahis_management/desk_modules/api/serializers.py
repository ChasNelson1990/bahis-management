from bahis_management.desk_modules.models import DeskModule, DeskModuleType
from rest_framework import serializers


class DeskModuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeskModuleType
        fields = ["id", "module_type"]


class DeskModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeskModule
        fields = [
            "id",
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
