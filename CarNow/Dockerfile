# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el contenido de la aplicación al contenedor
COPY . /app/

# Establecer la variable de entorno FLASK_APP para que Flask sepa dónde está la aplicación
ENV FLASK_APP=app.py

# Exponer el puerto donde Flask estará ejecutándose
EXPOSE 5000

# Definir el comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
