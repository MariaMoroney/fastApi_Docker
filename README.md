# API con FastAPI y Docker

Este repositorio contiene una API sencilla desarrollada con FastAPI y containerizada usando Docker.

## Descripción del Proyecto

Este proyecto fue desarrollado como parte del Trabajo Práctico 3 para el profesor Jorge Zapata. Consiste en una API básica que implementa varias rutas y está configurada para ejecutarse dentro de un contenedor Docker.

## Estructura del Proyecto

- `main.py`: Archivo principal que contiene la implementación de la API con FastAPI
- `requirements.txt`: Lista de dependencias necesarias para ejecutar la aplicación
- `Dockerfile`: Configuración para la creación de la imagen Docker

## Rutas Implementadas

- `/`: Ruta principal que devuelve un mensaje de bienvenida
- `/items/{item_id}`: Ruta que recibe un ID de ítem y opcionalmente un parámetro de consulta
- `/usuarios/{usuario_id}`: Ruta que devuelve información sobre un usuario específico

## Versionamiento

Este repositorio sigue una estructura de ramas basada en GitFlow:

- `main`: Rama principal para código en producción
- `staging`: Rama para pruebas antes de pasar a producción
- `develop`: Rama de desarrollo
- `feature/*`: Ramas para nuevas funcionalidades

## Instalación y Ejecución

### Requisitos Previos

- Python 3.11 o superior
- Docker

### Ejecución Local (sin Docker)

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/MariaMorey/fastApi_Docker.git
   cd fastApi_Docker
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación:
   ```bash
   uvicorn main:app --reload
   ```

5. Acceder a la API en [http://localhost:8000](http://localhost:8000)

### Ejecución con Docker

1. Construir la imagen:
   ```bash
   docker build -t mi-fastapi-app .
   ```

2. Ejecutar el contenedor:
   ```bash
   docker run -p 8000:8000 mi-fastapi-app
   ```

3. Acceder a la API en [http://localhost:8000](http://localhost:8000)

### Imagen en DockerHub

La imagen también está disponible en DockerHub y puede ser ejecutada directamente:

```bash
docker run -p 8000:8000 mariamoroney/mi-fastapi-docker:latest
```

## Documentación de la API

Una vez que la aplicación esté en ejecución, puedes acceder a la documentación automática en:

- [http://localhost:8000/docs](http://localhost:8000/docs) - Documentación Swagger UI
- [http://localhost:8000/redoc](http://localhost:8000/redoc) - Documentación ReDoc

## Autora

- María Fernanda Moroney Sole

## Enlaces

- [Repositorio en GitHub](https://github.com/MariaMoroney/fastApi_Docker.git)
- [Imagen en DockerHub](https://hub.docker.com/repository/docker/mariamoroney/mi-fastapi-docker/general)