# Usar una imagen oficial de Python como imagen base
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de dependencias al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto 8000 para que sea accesible desde fuera del contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn cuando el contenedor se inicie
# --host 0.0.0.0 es necesario para que sea accesible desde fuera del contenedor
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]