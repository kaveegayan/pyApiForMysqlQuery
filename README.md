# Simple MySQL REST API
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

##  Quickstart Guide

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
EXIT;
```
### 3. Create Python Virtual Environment & Install Dependencies:Isolate libraries using FastAPI, Uvicorn, and PyMySQL. 
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
### 4. Add the DB credential to .env file[for local testing]

```bash
vim .env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_secure_password
DB_NAME=company_db
```
#### Note: to prevent .env credentials commit to Git repo, add below lines to .gitignore file
```bash
vim .gitignore
.env
 pycache/
 *.pyc
```
### 5. Run the application 
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
### 6. Exit from the screen so application will run background 
```bash
#Press CTRL+A+D to exit
```
### 7. According the this Application, below end points are available to query using curl or postman
```bash
#search all records
curl http://localhost:8000/users
#search by user_id
curl http://localhost:8000/users/{id}
#search by name
curl http://localhost:8000/users/name/{user_name}
```
