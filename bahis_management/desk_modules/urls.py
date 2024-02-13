from bahis_management.desk_modules import views
from django.urls import path

app_name = "desk_modules"
urlpatterns = [
    path("", views.DeskModuleList.as_view(), name="list"),
    path("create", views.DeskModuleCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.DeskModuleUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeskModuleDelete.as_view(), name="delete"),
]
