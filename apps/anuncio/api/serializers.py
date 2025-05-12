from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.anuncio.models import Categoria, Anuncio, OfertaAnuncio


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre',
            'activa'
        ]

    def validate_nombre(self, value):
        # Verificar que el nombre no contegna la palabra "categoría"
        if "categoria" in value.lower():
            raise serializers.ValidationError("El nombre no puede contener la palabra 'categoria'.")
        return value


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = [
            'id',
            'titulo',
            'descripcion',
            'precio_inicial',
            'fecha_inicio',
            'fecha_fin',
            'activo',
            'categorias',
            'publicado_por',
            'oferta_ganadora'
        ]
        read_only_fields = ['publicado_por', 'oferta_ganadora']


class OfertaAnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfertaAnuncio
        fields = '__All__'

    def validate(self, data):
        # Validar si el precio de la oferta es mayor que el precio inicial del anuncio
        if data['precio_oferta'] <= data['precio_inicial']:
            raise ValidationError("La oferta debe ser mayor al precio inicial del artículo.")

        return data
