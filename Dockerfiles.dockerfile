# Dockerfile para servicios_usuarios
FROM python:3.13
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "servicios_usuarios.py"]
