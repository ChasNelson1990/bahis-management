from bahis_management.taxonomies import views
from django.urls import path

app_name = "taxonomies"
urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.TaxonomyList.as_view(), name="list"),
    path("create/", views.TaxonomyCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.TaxonomyUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", views.TaxonomyDelete.as_view(), name="delete"),
    path("regions/", views.AdministrativeRegionList.as_view(), name="adminstrative_region_list"),
    path("regions/create/", views.AdministrativeRegionCreate.as_view(), name="adminstrative_region_create"),
    path("regions/update/<int:pk>/", views.AdministrativeRegionUpdate.as_view(), name="adminstrative_region_update"),
    path("regions/delete/<int:pk>/", views.AdministrativeRegionDelete.as_view(), name="adminstrative_region_delete"),
    path("regions/levels/", views.AdministrativeRegionLevelList.as_view(), name="adminstrative_region_level_list"),
    path(
        "regions/levels/create/",
        views.AdministrativeRegionLevelCreate.as_view(),
        name="adminstrative_region_level_create",
    ),
    path(
        "regions/levels/update/<int:pk>/",
        views.AdministrativeRegionLevelUpdate.as_view(),
        name="adminstrative_region_level_update",
    ),
    path(
        "regions/levels/delete/<int:pk>/",
        views.AdministrativeRegionLevelDelete.as_view(),
        name="adminstrative_region_level_delete",
    ),
]
