#!/bin/bash

# Esperar hasta que MySQL esté disponible
until nc -z -v -w30 db 3306; do
  echo "Esperando a que MySQL esté disponible..."
  sleep 1
done

# Ejecutar makemigrations
echo "Ejecutando makemigrations..."
python manage.py makemigrations

# Verificar si la variable de entorno MIGRATE está configurada para ejecutar migrate
if [ "$MIGRATE" == "true" ]; then
  echo "Ejecutando migrate..."
  python manage.py migrate
else
  echo "No se ejecutó migrate, establezca MIGRATE=true para ejecutarlo."
fi

# Ejecutar el servidor de Django
echo "Iniciando el servidor de Django..."
python manage.py runserver 0.0.0.0:8000
