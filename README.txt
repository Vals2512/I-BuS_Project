# I-BuS: Sistema Django conectado a MySQL
Este proyecto contiene un sistema web desarrollado en Django con autenticación personalizada basada en tu tabla `Usuario` en MySQL.

## Requisitos
- Python 3.13
- MySQL (con base de datos `ibus_db` y usuario `root`)
- pip install -r requirements.txt

## Ejecutar localmente
1. Clona el proyecto o descomprime este archivo.
2. Ejecuta las migraciones necesarias (si las hay).
3. Inicia el servidor con:
```bash
python manage.py runserver
```

## Próximo paso
Desplegar con Docker.
