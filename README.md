# Aruba API Explorer

Herramienta educativa para explorar Aruba Central VisualRF, comprender la jerarquía Campus → Buildings → Floors y consultar ubicaciones de clientes y Access Points.

## Arquitectura

- **Frontend:** HTML, CSS y JavaScript estático.
- **Backend:** Python + FastAPI.
- **Aruba Central:** las credenciales y llamadas a la API se gestionarán exclusivamente desde el backend.

> No guardes Client Secret, Refresh Token ni tokens de acceso en este repositorio. Usa variables de entorno en el backend.

## Estructura

```
frontend/
  index.html
  css/styles.css
  js/app.js
backend/
  main.py
  aruba_api.py
  config.py
  requirements.txt
.env.example
.gitignore
README.md
```

## Desarrollo local

1. Crea un entorno virtual de Python.
2. Instala dependencias desde `backend/requirements.txt`.
3. Copia `.env.example` a `.env` y completa la configuración local cuando se habilite la integración.
4. Ejecuta el backend desde la carpeta `backend` con:

```bash
uvicorn main:app --reload
```

5. Abre `frontend/index.html` en el navegador o sírvelo con un servidor estático.

El backend de esta primera versión solo ofrece un endpoint de estado. La autenticación OAuth 2.0 y los endpoints VisualRF se implementarán y validarán en etapas posteriores.

## Seguridad

- Nunca publiques archivos `.env`.
- No introduzcas secretos en JavaScript del navegador.
- No compartas tokens ni capturas que los expongan.
- Usa HTTPS y controles de acceso antes de desplegar el backend en producción.
