# API Departamento de Extraescolares

Este proyecto contiene una API REST para la gestión de actividades extraescolares. El contenedor Docker incluye la aplicación y todas sus dependencias.

## Requisitos

- Docker

## Instrucciones para construir y ejecutar el contenedor

1. Clona el repositorio:
   
   - git clone https://github.com/usuario/nombre-repositorio](https://github.com/IvanPorrasMacias/API_DepartamentoExtraescolares.git
   - cd API_DepartamentoExtraescolares

2. Construye la imagen en Docker:

   - docker build -t api_extraescolares .

3. Corre el contenedor:

   - docker run -d -p 8000:8000 api_extraescolares

4. Accede a la API en tu navegador:

   - http://localhost:8000

## También puedes encontrar el contenedor directamente en DockerHub

   - docker pull ivanporra5/api_extraescolares:latest
   - docker run -d -p 8000:8000 ivanporra5/api_extraescolares


