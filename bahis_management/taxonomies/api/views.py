from bahis_management.taxonomies.api.serializers import (
    AdministrativeRegionLevelSerializer,
    AdministrativeRegionSerializer,
    TaxonomySerializer,
)
from bahis_management.taxonomies.models import (
    AdministrativeRegion,
    AdministrativeRegionLevel,
    Taxonomy,
)
from rest_framework import parsers, permissions, viewsets


class TaxonomyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows custom Taxonomies to be viewed or edited.
    """

    queryset = Taxonomy.objects.all().order_by("slug")
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    serializer_class = TaxonomySerializer
    permission_classes = [permissions.AllowAny]  # [permissions.IsAuthenticated] FIXME auth is turned off


class AdministrativeRegionLevelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AdministrativeRegionLevels to be viewed or edited.
    """

    queryset = AdministrativeRegionLevel.objects.all().order_by("id")
    serializer_class = AdministrativeRegionLevelSerializer
    permission_classes = [permissions.AllowAny]  # [permissions.IsAuthenticated] FIXME auth is turned off


class AdministrativeRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AdministrativeRegions to be viewed or edited.
    """

    queryset = AdministrativeRegion.objects.all().order_by("id")
    serializer_class = AdministrativeRegionSerializer
    permission_classes = [permissions.AllowAny]  # [permissions.IsAuthenticated] FIXME auth is turned off
