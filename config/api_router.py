from bahis_management.desk_modules.api.views import (
    DeskModuleListDefinitionViewSet,
    DeskModuleTypeViewSet,
    DeskModuleViewSet,
    DeskModuleWorkflowViewSet,
)
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("desk/modules", DeskModuleViewSet)
router.register("desk/module-types", DeskModuleTypeViewSet)
router.register("desk/list-definitions", DeskModuleListDefinitionViewSet)
router.register("desk/workflows", DeskModuleWorkflowViewSet)

app_name = "api"
urlpatterns = router.urls
