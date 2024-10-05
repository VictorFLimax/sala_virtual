from rest_framework.routers import DefaultRouter

from core import viewsets

router = DefaultRouter()
router.register('anexo', viewsets.AnexoViewSet)



urlpatterns = router.urls