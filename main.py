# main.py
from fastapi import FastAPI, HTTPException, Body
import random
import time
import psutil

app = FastAPI(
    title="API de demo",
    description="API para simular disponibilidad de una aplicación y ajustar el uptime.",
    version="1.0"
)

# Variable global para el delay
max_delay_ms = 0

@app.get(
    "/saludo",
    summary="Obtener saludo que demora según cierto delay",
    description="Devuelve un mensaje de saludo que demora según el delay configurado.",
    response_description="Mensaje de saludo con cierto delay"
)
def saludo():
    global max_delay_ms
    inicio = time.time()
    delay = random.uniform(0, max_delay_ms) / 1000  # convertir a segundos
    time.sleep(delay)
    fin = time.time()
    return {
        "mensaje": "¡Hola!",
        "delay_real_ms": delay * 1000,
        "tiempo_respuesta_ms": (fin - inicio) * 1000,
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memoria_mb": psutil.virtual_memory().used / (1024 * 1024)
    }

@app.post(
    "/set-max-delay",
    summary="Ajustar el valor de delay del sistema",
    description="Permite establecer el valor de delay (en milisegundos) que demora el sistema en responder.",
    response_description="Mensaje de confirmación o error de validación"
)
def set_max_delay(value: int = Body(..., embed=True)):
    global max_delay_ms
    if value >= 0:
        max_delay_ms = value
    else:
        raise HTTPException(status_code=400, detail="El valor debe ser mayor o igual a 0")
        uptime_value = value
    return {"mensaje": f"Delay actualizado a {max_delay_ms}"}