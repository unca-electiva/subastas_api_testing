from datetime import datetime, timedelta, timezone

import pytest

from .fixtures_categoria import get_categoria
from .fixtures_user import get_authenticated_client, get_user_generico, api_client


def test_foo():
    assert True


def test_lista():
    assert list(reversed([1, 2, 3])) == [3, 2, 1]


@pytest.mark.django_db
def test_api_crear_anuncio_falla_fecha_inicio_anterior_actual(mocker, get_authenticated_client, get_categoria):
    # Simulamos que "ahora" es 2025-06-12 12:00:00
    fecha_actual_mock = datetime(2025, 6, 12, 12, 0, 0, tzinfo=timezone.utc)
    mocker.patch('django.utils.timezone.now', return_value=fecha_actual_mock)

    data = {
        "titulo": "Mesa living",
        "descripcion": "Mesa ratona de living con vidrio",
        "precio_inicial": "150500.00",
        "fecha_inicio": fecha_actual_mock - timedelta(days=1),  # un día antes del "ahora" simulado
        "fecha_fin": fecha_actual_mock + timedelta(days=5),
        "categorias": [get_categoria.id]
    }

    cliente = get_authenticated_client

    response = cliente.post(f'/api/anuncio/', data=data)

    assert response.status_code == 400
    assert str(response.data['fecha_inicio'][0]) == "La Fecha de Inicio no puede ser anterior a la Fecha Actual."
