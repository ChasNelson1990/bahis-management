from bahis_management.desk_modules.models import (
    DeskModule,
    DeskModuleListDefinition,
    DeskModuleType,
    DeskModuleWorkflow,
)
from rest_framework import serializers


class DeskModuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeskModuleType
        fields = ["id", "title"]


class DeskModuleListDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeskModuleListDefinition
        fields = [
            "id",
            "title",
            "form_id",
            "column_definitions",
            "filter_definitions",
        ]


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


class DeskModuleWorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeskModuleWorkflow
        fields = [
            "id",
            "title",
            "list_id",
            "form_id",
            "workflow_definition",
            "is_active",
        ]
