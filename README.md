# Proyecto FastAPI con Redis y Docker

Este es un proyecto de ejemplo simple que utiliza FastAPI y Redis. Está configurado para ser ejecutado con Docker y Docker Compose, sirviendo como una práctica básica para entender cómo orquestar contenedores con una API moderna.

La API es un contador de visitas que utiliza Redis para persistir el número de veces que se ha consultado un endpoint.

## Requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Cómo ejecutar el proyecto 🚀

1. Clona este repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-directorio>
   ```

2. Levanta los servicios utilizando `docker-compose`:
   ```bash
   docker-compose up --build
   ```
   Esto construirá la imagen para la aplicación FastAPI y levantará dos contenedores: uno para la API (`web`) y otro para la base de datos Redis (`redis`).

3. Abre tu navegador y visita `http://localhost:8000`.

   Deberías ver una respuesta JSON como: `{"mensaje":"Este endpoint ha sido visitado X veces."}`. El número `X` se incrementará cada vez que recargues la página.

4. **Explora la documentación interactiva** (¡una de las grandes ventajas de FastAPI!):
   - **Swagger UI**: `http://localhost:8000/docs`
   - **ReDoc**: `http://localhost:8000/redoc`

## Funcionamiento

- **`app.py`**: Contiene la lógica de la API con FastAPI. Se conecta a Redis, incrementa el contador de forma atómica y devuelve el resultado en formato JSON.
- **`Dockerfile`**: Define la imagen de Docker para la aplicación. Instala las dependencias de Python (`fastapi`, `uvicorn` y `redis`) y establece el comando para iniciar el servidor ASGI `Uvicorn`.
- **`docker-compose.yaml`**: Orquesta los contenedores. Define dos servicios:
    - `web`: La API de FastAPI.
    - `redis`: La base de datos Redis.
  La API puede comunicarse con el servicio de Redis utilizando el nombre de host `redis`, que es el nombre del servicio en el archivo `docker-compose.yaml`.

## Estructura del Proyecto

```
.
├── app.py                # Aplicación principal de Flask
├── Dockerfile            # Define la imagen de la aplicación
├── requirements.txt      # Dependencias de Python
└── docker-compose.yaml   # Orquestación de los contenedores
```


Curso de Docker para Desarrolladores:
https://www.desarrollolibre.net/blog/docker/guia-para-principiantes-para-docker#heading-23