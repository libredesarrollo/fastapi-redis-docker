from fastapi import FastAPI
import redis
import os

app = FastAPI(
    title="Contador de Visitas con FastAPI y Redis",
    description="Un API simple que incrementa un contador en Redis.",
    version="1.0.0",
)

# Conectarse a Redis usando el nombre del servicio 'localhost' de docker-compose
# Se usa una variable de entorno para flexibilidad, con 'localhost' como valor por defecto.
redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)


@app.get("/", summary="Incrementar y obtener contador de visitas")
def get_visits():
    """
    Incrementa un contador en Redis y devuelve el número total de visitas.
    """
    try:
        visits = r.incr('visits')
    except redis.exceptions.ConnectionError as e:
        return {
            "error": "No se pudo conectar a Redis",
            "tried_host": redis_host,
            "details": str(e)
        }
    return {"mensaje": f"Este endpoint ha sido visitado {visits} veces."}