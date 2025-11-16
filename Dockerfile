# Imagen base de Python
FROM python:3.10-slim

# Crear directorio para la app
WORKDIR /app

# Copiar requisitos
COPY src/requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación completa
COPY src/ .

# Exponer el puerto del servidor Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
