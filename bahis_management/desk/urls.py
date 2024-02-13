from django.urls import path

from bahis_management.desk import views

app_name = "desk"
urlpatterns = [
    path("", views.ModuleList.as_view(), name="list"),
    path("create", views.ModuleCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.ModuleUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", views.ModuleDelete.as_view(), name="delete"),
    path("list-definitons/", views.ModuleListDefinitionList.as_view(), name="list"),
    path("list-definitons/create", views.ModuleListDefinitionCreate.as_view(), name="create"),
    path("list-definitons/update/<int:pk>/", views.ModuleListDefinitionUpdate.as_view(), name="update"),
    path("list-definitons/delete/<int:pk>/", views.ModuleListDefinitionDelete.as_view(), name="delete"),
    path("workflows/", views.ModuleWorkflowList.as_view(), name="list"),
    path("workflows/create", views.ModuleWorkflowCreate.as_view(), name="create"),
    path("workflows/update/<int:pk>/", views.ModuleWorkflowUpdate.as_view(), name="update"),
    path("workflows/delete/<int:pk>/", views.ModuleWorkflowDelete.as_view(), name="delete"),
]
