FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    python3-dev \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && apt-get clean

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Copiar el archivo entrypoint.sh al contenedor
COPY entrypoint.sh /entrypoint.sh

# Dar permisos de ejecución al script
RUN chmod +x /entrypoint.sh

# Configurar el contenedor para que ejecute entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

