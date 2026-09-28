# Python  MySQL REST API
A lightweight RESTful API built with **Python**, **FastAPI**, and **PyMySQL** to query user records from a MySQL database using environment-based configurations.
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Tech Stack & Prerequisites

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Database:** MySQL 8.0+
* **Database Driver:** PyMySQL
* **ASGI Server:** Uvicorn

---
### There are two methods you can deploy this application
### METHOD A: Deploy directly on linux server
### METHOD B: Deploy on docker container 
---
### Below Steps are essential to both methods

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/pyApiForMysqlQuery.git]
cd pyApiForMysqlQuery
```
### 2. Database Setup
#### Log into your MySQL server and run the following script to create the database, table, and sample records:
```bash
mysql -u root -p
```
```sql
---create databese
CREATE DATABASE company_db;
---loging to the database
USE company_db;
---create the users table
CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, role VARCHAR(50) NOT NULL );
---insert sample data
INSERT INTO users (name, email, role) VALUES ('Kavee Smith', 'kavee@abc.com', 'DevOps Engineer');
---create DB connection user and grant previlige
CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY 'DB_secure_password';
GRANT ALL PRIVILEGES ON company_db.* TO 'root'@'%';
FLUSH PRIVILEGES;

EXIT;
```
### 3. Add the DB credential to .env file[for local testing]

```bash
vim .env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_secure_password
DB_NAME=company_db
```
#### Note: to prevent .env credentials commit to Git repo, Make sure add below lines(all sensitive data) to .gitignore file
```bash
vim .gitignore
.env
 pycache/
 *.pyc
venv/
```
##  METHOD A: Quickstart Guide to deploy directly on linux server

### 1. Create Python Virtual Environment & Install Dependencies:Isolate libraries using FastAPI, Uvicorn, and PyMySQL. 
#### Open your terminal and run:
```bash
# Go to project directroy
cd pyApiForMysqlQuery
```
```bash
# Install virtual environment
apt install python3.12-venv
# Create and activate virtual environment
python3 -m venv venv source venv/bin/activate
# Install FastAPI, Uvicorn (web server), and PyMySQL
pip install fastapi uvicorn pymysql
#install dot .env to safely pass credentials
pip install python-dotenv
```
### 2. Run the application 
```bash
# Open a Screen to run the application on background
screen -S pyapi
```
```bash
# Go to project directory and activate virtual environment here(Because you opened a new screen terminal, need to re activate)
# Run below commands
cd pyApiForMysqlQuery
source venv/bin/activate
```
```bash
# Run application using port 8000
uvicorn main:app --reload --port 8000
```
### 3. Exit from the screen so application will run background 
```bash
#Press CTRL+A+D to exit
```
### 4. According the this Application, below end points are available to query using curl or postman
```bash
#search all records
curl http://localhost:8000/users
#search by user_id
curl http://localhost:8000/users/{id}
#search by name
curl http://localhost:8000/users/name/{user_name}
```

## METHOD B: Quickstart Guide to deploy on docker container

### 1. Change the mysql bind address to accept connection from docker container

```bash
vim /etc/mysql/mysql.conf.d/mysqld.cnf
# Change bind address
bind-address = 0.0.0.0
# Restart mysql to apply changes
systemctl restart mysql

```
### 2. Add .dockerignore file to prevent copy unwanted files to docker container
```bash
vim .dockerignore
__pycache__/
*.pyc
*.pyo
venv/
.env
.git/
.gitignore
```
### 3. Build docker image
```bash
#Run below build command
docker build -t fastapi-mysql-api .
```
### 4. Start Docker Container
```bash
# you can pass related parameters as arguments
docker run -d \
  -p 8000:8000 \
  -e DB_HOST="host.docker.internal" \
  -e DB_USER="root" \
  -e DB_PASSWORD="DB_secure_password" \
  -e DB_NAME="company_db" \
  --add-host=host.docker.internal:host-gateway \
  fastapi-mysql-api
# Note:
1. DB_HOST="host.docker.internal" and --add-host=host.docker.internal:host-gateway parameters forcing Docker to use Hosting server IP as DB ip sice mysql seperately hosted in Host server
2. In production environments not safe to pass the credentials as an argument, as an engineer i use "AWS secret Manager" and import boto3 in python app to get credentials safe
```
```bash
# run below command to see if docker container started
docker ps
# run below command to see the container logs
docker logs -f <container_id>
```
### 5. According the this Application, below end points are available to query using curl or postman
```bash
#search all records
curl http://localhost:8000/users
#search by user_id
curl http://localhost:8000/users/{id}
#search by name
curl http://localhost:8000/users/name/{user_name}
```

