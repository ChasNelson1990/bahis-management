from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from bahis_management.desk_modules.api.views import DeskModulesViewSet, DeskModuleTypeViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("desk/modules", DeskModulesViewSet)
router.register("desk/module-types", DeskModuleTypeViewSet)

app_name = "api"
urlpatterns = router.urls
