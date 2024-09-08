from django.urls import include, path
from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.BahisLoginView.as_view(), name="index"),
    path("", include("django.contrib.auth.urls")),
]
