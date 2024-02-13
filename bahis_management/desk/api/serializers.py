from bahis_management.desk.models import (
    Module,
    ModuleListDefinition,
    ModuleType,
    ModuleWorkflow,
)
from rest_framework import serializers


class ModuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleType
        fields = ["id", "title"]


class ModuleListDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleListDefinition
        fields = [
            "id",
            "title",
            "form_id",
            "column_definitions",
            "filter_definitions",
        ]


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
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


class ModuleWorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleWorkflow
        fields = [
            "id",
            "title",
            "list_id",
            "form_id",
            "workflow_definition",
            "is_active",
        ]
