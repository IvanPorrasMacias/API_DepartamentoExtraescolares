# API Departamento de Extraescolares

Este proyecto contiene una API REST para la gestión de actividades extraescolares. El contenedor Docker incluye la aplicación y todas sus dependencias.

## Requisitos

- Docker

## Instrucciones para construir y ejecutar el contenedor

1. Clona el repositorio:
   
       git clone https://github.com/usuario/nombre-repositorio](https://github.com/IvanPorrasMacias/API_DepartamentoExtraescolares.git
       cd API_DepartamentoExtraescolares

2. Construye la imagen en Docker:

       docker build -t api_extraescolares .

3. Corre el contenedor:

       docker run -d -p 8000:8000 api_extraescolares

4. Accede a la API en tu navegador:

   - http://localhost:8000

## También puedes encontrar el contenedor directamente en DockerHub

     docker pull ivanporra5/api_extraescolares:latest
     docker run -d -p 8000:8000 ivanporra5/api_extraescolares

## Correr el contenedor en un servidor de Jenkins

1. Crea un Pipeline e inserta el siguiente script

![image](https://github.com/user-attachments/assets/0a31910a-fa19-45a9-bd7f-368005bd4673)

        pipeline {
        agent any
        stages {
        stage('Pull Docker Image') {
             steps {
                 script {
                     sh 'docker pull ivanporra5/api_extraescolares:latest'
                 }
             }
         }
         stage('Run Docker Container') {
             steps {
                 script {
                     sh 'docker run -d -p 8000:8000 ivanporra5/api_extraescolares'
                 }
             }
         }
         }
         }
   
3. Ejecuta el pipeline y ahora puedes realizar pruebas con Postman

![image](https://github.com/user-attachments/assets/84e3f1ef-ad81-46e1-be74-6f0a77bbd39f)

A continuación se muestran algunos ejemplos

- POST alumno

![image](https://github.com/user-attachments/assets/4b79be8a-ef10-45a5-91ff-8e2f0e600f25)

- GET alumno por su número de control

![image](https://github.com/user-attachments/assets/2157f273-7529-4005-bb9b-e950b96c5383)

- PATCH alumno por su número de control

![image](https://github.com/user-attachments/assets/72be4bcf-fdf7-4d94-9d87-7e3bcdd65a60)

- DELETE alumno por su número de control

![image](https://github.com/user-attachments/assets/034457b2-b9c9-4d16-96a2-1cb0dfdd7108)

- POST actividad

![image](https://github.com/user-attachments/assets/acd4222d-7176-4469-a365-959c4d4a79fe)

- GET actividad por su id

![image](https://github.com/user-attachments/assets/2a5095d9-3fe9-4478-adf1-14d45b599bc6)

- PATCH actividad por su id

![image](https://github.com/user-attachments/assets/ad05b391-771b-43db-b01d-417628065593)

- DELETE actividad por su id

![image](https://github.com/user-attachments/assets/8c07082d-1656-4c7e-98c5-a90d3aa723bf)

- POST actividades_alumno

![image](https://github.com/user-attachments/assets/4d35b877-4a94-40cd-a86c-00e39ab3e22e)

- GET actividades_alumno por su id

![image](https://github.com/user-attachments/assets/db130f51-4f6d-43a7-9e1e-04b88fcecd88)

- PATCH actividades_alumno por su id

![image](https://github.com/user-attachments/assets/30eebc5f-61d9-45ff-a1d9-a4ffaffe4391)

- DELETE actividades_alumno por su id

![image](https://github.com/user-attachments/assets/613b7aaa-2f11-4eed-8c2b-f8668ce12464)

## Créditos a todos los colaboradores

- Ivan Porras Macias
- Brandon Aguiñaga Castañeda
- Kevin Jesús Martín Lopez Doblado
- Erik Uriel Lopez Salinas

