from bahis_management.desk.api.views import (
    ModuleListDefinitionViewSet,
    ModuleTypeViewSet,
    ModuleViewSet,
    ModuleWorkflowViewSet,
)
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("desk/modules", ModuleViewSet)
router.register("desk/module-types", ModuleTypeViewSet)
router.register("desk/list-definitions", ModuleListDefinitionViewSet)
router.register("desk/workflows", ModuleWorkflowViewSet)

app_name = "api"
urlpatterns = router.urls
