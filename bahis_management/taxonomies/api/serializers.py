from bahis_management.taxonomies.models import (
    AdministrativeRegion,
    AdministrativeRegionLevel,
    Taxonomy,
)
from rest_framework import serializers


class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = ["id", "title", "slug", "csv_file"]


class AdministrativeRegionLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeRegionLevel
        fields = ["id", "title"]


class AdministrativeRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeRegion
        fields = [
            "id",
            "title",
            "administrative_region_level",
            "parent_administrative_region",
        ]
