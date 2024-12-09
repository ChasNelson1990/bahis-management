from rest_framework import serializers

from nexus.desk.models import Module, ModuleType, Workflow


class ModuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleType
        fields = ["id", "title"]


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = [
            "id",
            "title",
            "icon",
            "description",
            "form",
            "external_url",
            "module_type",
            "parent_module",
            "sort_order",
            "is_active",
        ]


class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = [
            "id",
            "title",
            "source_form",
            "destination_form",
            "definition",
            "is_active",
        ]
