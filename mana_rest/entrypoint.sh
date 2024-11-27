#!/bin/bash

# Esperar hasta que MySQL esté disponible
until nc -z -v -w30 db 3306; do
  echo "Esperando a que MySQL esté disponible..."
  sleep 1
done

# Ejecutar el servidor de Django
echo "Iniciando el servidor de Django..."
python manage.py runserver 0.0.0.0:8000
