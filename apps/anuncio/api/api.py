from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .filters import CategoriaFilter
from .serializers import CategoriaSerializer, AnuncioSerializer
from ..models import Categoria, Anuncio


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CategoriaFilter
    ordering_fields = ['nombre', 'activa']


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    def perform_create(self, serializer):
        serializer.save(publicado_por=self.request.user)
