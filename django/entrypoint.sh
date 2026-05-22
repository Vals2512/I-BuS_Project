#!/bin/sh
set -e

echo "==============================="
echo "  IBuS — Iniciando servidor"
echo "==============================="

echo "Aplicando migraciones..."
python manage.py migrate --noinput

echo "Cargando datos iniciales..."
if [ -f "datos_iniciales.json" ]; then
    python manage.py loaddata datos_iniciales.json && echo "Datos cargados correctamente" || echo "Datos ya existentes, omitiendo"
fi

echo "Servidor corriendo en http://localhost:8000"
python manage.py runserver 0.0.0.0:8000
