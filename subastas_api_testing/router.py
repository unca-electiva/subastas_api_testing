from rest_framework import routers
from apps.anuncio.api import api

# Initializar el router de DRF solo una vez
router = routers.DefaultRouter()

# Registrar un ViewSet
router.register(prefix='categoria', viewset=api.CategoriaViewSet)
router.register(prefix='anuncio', viewset=api.AnuncioViewSet)

urlpatterns = [
]

urlpatterns += router.urls
