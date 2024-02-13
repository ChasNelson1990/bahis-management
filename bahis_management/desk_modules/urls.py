from django.urls import path

from bahis_management.desk_modules import views

app_name = "desk_modules"
urlpatterns = [
    path("", views.DeskModuleList.as_view(), name="list"),
    path("create", views.DeskModuleCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.DeskModuleUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeskModuleDelete.as_view(), name="delete"),
    path("list-definitons/", views.DeskModuleListDefinitionList.as_view(), name="list"),
    path("list-definitons/create", views.DeskModuleListDefinitionCreate.as_view(), name="create"),
    path("list-definitons/update/<int:pk>/", views.DeskModuleListDefinitionUpdate.as_view(), name="update"),
    path("list-definitons/delete/<int:pk>/", views.DeskModuleListDefinitionDelete.as_view(), name="delete"),
    path("workflows/", views.DeskModuleWorkflowList.as_view(), name="list"),
    path("workflows/create", views.DeskModuleWorkflowCreate.as_view(), name="create"),
    path("workflows/update/<int:pk>/", views.DeskModuleWorkflowUpdate.as_view(), name="update"),
    path("workflows/delete/<int:pk>/", views.DeskModuleWorkflowDelete.as_view(), name="delete"),
]
