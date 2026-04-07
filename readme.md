# QA Fintech Lab

Mini laboratorio de pruebas QA simulando una API fintech.

## Tecnologías
- Python
- Pytest
- Requests
- JSON Server

## Qué se valida
- Status code de endpoints
- Estructura de respuesta
- Campos obligatorios
- Integridad entre cuentas y transacciones

## Cómo correr el proyecto

1. Levantar API mock:
```bash
npx json-server --watch db.json --port 3000