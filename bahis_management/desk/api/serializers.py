from bahis_management.desk.models import (
    Module,
    ListDefinition,
    ModuleType,
    Workflow,
)
from rest_framework import serializers


class ModuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleType
        fields = ["id", "title"]


class ListDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListDefinition
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


class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = [
            "id",
            "title",
            "list_id",
            "form_id",
            "workflow_definition",
            "is_active",
        ]
