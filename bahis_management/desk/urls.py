from django.urls import path

from bahis_management.desk import views

app_name = "desk"
urlpatterns = [
    path("", views.ModuleList.as_view(), name="list"),
    path("create", views.ModuleCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.ModuleUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", views.ModuleDelete.as_view(), name="delete"),
    path("list-definitons/", views.ListDefinitionList.as_view(), name="list"),
    path("list-definitons/create", views.ListDefinitionCreate.as_view(), name="create"),
    path("list-definitons/update/<int:pk>/", views.ListDefinitionUpdate.as_view(), name="update"),
    path("list-definitons/delete/<int:pk>/", views.ListDefinitionDelete.as_view(), name="delete"),
    path("workflows/", views.WorkflowList.as_view(), name="list"),
    path("workflows/create", views.WorkflowCreate.as_view(), name="create"),
    path("workflows/update/<int:pk>/", views.WorkflowUpdate.as_view(), name="update"),
    path("workflows/delete/<int:pk>/", views.WorkflowDelete.as_view(), name="delete"),
]
