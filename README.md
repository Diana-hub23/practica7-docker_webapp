# 📘 Práctica 7 – Web App Flask + MySQL con Docker Compose

Para esta práctica desarrollé una aplicación web en **Python (Flask)** que muestra un mensaje tipo **"Hola Mundo"** y se conecta correctamente a una base de datos **MySQL**, todo ejecutado mediante **Docker Compose**.

---

## ✔️ a) Estructura del proyecto

practica7-docker_webapp/
│ Dockerfile
│ docker-compose.yml
└── src/
app.py
database.py
requirements.txt

---

## ✔️ b) Archivo docker-compose.yml

Incluye dos servicios principales:

### **1. web (Flask)**  
- Construido con el Dockerfile  
- Expone el puerto 5000  
- Usa variables de entorno para conectarse a MySQL  
- Depende del servicio MySQL

### **2. mysql (MySQL 8.0)**  
- Crea la base de datos `testdb`  
- Usa contraseña del root  
- Expone el puerto 3306  
- Utiliza un volumen persistente `mysql_data`

Para ejecutar todo:

docker compose up --build

---

## ✔️ c) Servicio del servidor de aplicación (Flask)

La app está construida con:

- **Python 3.10**
- **Flask**
- Conexión a MySQL mediante `mysql-connector-python`

El Dockerfile:
- Instala dependencias
- Copia el código
- Ejecuta la aplicación en el puerto 5000

---

## ✔️ d) Servicio de base de datos MySQL

El contenedor MySQL configura:

- Usuario root con contraseña personalizada  
- Base de datos inicial `testdb`  
- Persistencia con volumen Docker  
- Puerto expuesto 3306  

---

## 🔗 Repositorio del proyecto

https://github.com/Diana-hub23/practica7-docker_webapp
