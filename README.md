<img src="https://www.ucu.edu.uy/plantillas/images/logo_ucu.svg" alt="UCU"
width="200"/>

# Universidad Católica del Uruguay

## Facultad de Ingeniería y Tecnologías

### Análisis y diseño de aplicaciones II

<br/>

# Demo de rendimiento

Esta demo tiene una sencilla [aplicación web](./main.py) que expone una API
REST; está implementada en Python usando [fastapi](https://fastapi.tiangolo.com)
y la ejecutamos con [uvicorn](https://www.uvicorn.org).

La API tiene un endpoint para devolver un saludo que demora cierto tiempo que se
puede configurar; el valor predeterminado es 0 indicando que no hay demora.

El otro endpoint de la API permite cambiar la probabilidad por un valor entre 0
y 1.

La demo incluye también los scripts de
[K6](https://grafana.com/docs/k6/latest/set-up/install-k6/) para probarla.

Para ejecutar esta demo usa los comandos que están [aquí](./commands.azcli). Con
el complemento [Azure CLI
Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azurecli)
es posible ejecutar los comandos directamente desde Visual Studio Code.

Una vez que ejecutes la aplicación, puedes ver la documentación de los endpoints
con [Swagger](http://localhost:5001/docs).

# Requisitos

* Python

* [K6](https://grafana.com/docs/k6/latest/set-up/install-k6/)

# Actividades

A partir de los resultados de K6 y utilizando diferentes valores de demora,
analiza cómo impacta el rendimiento.
