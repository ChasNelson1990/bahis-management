from bahis_management.desk.api.views import (
    ModuleTypeViewSet,
    ModuleViewSet,
    WorkflowViewSet,
)
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("desk/modules", ModuleViewSet)
router.register("desk/module-types", ModuleTypeViewSet)
router.register("desk/workflows", WorkflowViewSet)

app_name = "api"
urlpatterns = router.urls
