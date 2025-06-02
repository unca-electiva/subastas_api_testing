# subastas_api_testing

## Descripción

Este proyecto consiste en una API desarrollada con Django y Django REST Framework para la gestión de subastas, anuncios y categorías. El objetivo principal es la implementación y práctica de testing automatizado sobre la API, utilizando herramientas como pytest y pytest-django.

## Características principales

- Gestión de usuarios personalizados.
- Gestión de anuncios y categorías con relaciones y validaciones.
- Autenticación basada en tokens.
- Filtros y búsquedas sobre los endpoints de la API.
- Testing automatizado de endpoints y lógica de negocio usando pytest y pytest-django.
- Configuración especial para testing con base de datos en memoria y desactivación de migraciones para mayor velocidad.

## Estructura relevante

- `apps/usuario`: Gestión de usuarios.
- `apps/anuncio`: Gestión de anuncios, categorías y ofertas.
- `subastas_api_testing`: Configuración principal del proyecto.
- `apps/anuncio/tests`: Pruebas automatizadas y fixtures.

## Ejecución de tests

Para ejecutar los tests automatizados:

```sh
pytest .
```

La configuración de testing utiliza una base de datos en memoria y desactiva las migraciones para mayor velocidad.

## Dependencias principales

- Django
- djangorestframework
- django-filter
- pytest
- pytest-django

## Objetivo

El foco del proyecto es el desarrollo de una API robusta y la implementación de pruebas automatizadas para garantizar su correcto funcionamiento y facilitar el mantenimiento del código.