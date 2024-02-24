from django.urls import path

from bahis_management.desk import views

app_name = "desk"
urlpatterns = [
    path("", views.ModuleList.as_view(), name="list"),
    path("create", views.ModuleCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.ModuleUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", views.ModuleDelete.as_view(), name="delete"),
    path("list-definitions/", views.ListDefinitionList.as_view(), name="list_definitions_list"),
    path("list-definitions/create", views.ListDefinitionCreate.as_view(), name="list_definitions_create"),
    path("list-definitions/update/<int:pk>/", views.ListDefinitionUpdate.as_view(), name="list_definitions_update"),
    path("list-definitions/delete/<int:pk>/", views.ListDefinitionDelete.as_view(), name="list_definitions_delete"),
    path("workflows/<list_definition_id>", views.WorkflowList.as_view(), name="workflows_list"),
    path("workflows/create", views.WorkflowCreate.as_view(), name="workflows_create"),
    path("workflows/update/<int:pk>/", views.WorkflowUpdate.as_view(), name="workflows_update"),
    path("workflows/delete/<int:pk>/", views.WorkflowDelete.as_view(), name="workflows_delete"),
]
