from rest_framework.routers import DefaultRouter
from .api import ProyectoViewSet

router = DefaultRouter()
router.register('api/proyecto', ProyectoViewSet, 'proyecto')

urlpatterns = router.urls