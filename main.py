# ======== Kavee's API=============####
#Python API application to Get the information from a mysql DB
#imporing SDKs
import os
from fastapi import FastAPI, HTTPException
import pymysql
import pymysql.cursors
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Simple MySQL API")

# Database configuration loaded safely from environment variables
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "company_db"),
    "cursorclass": pymysql.cursors.DictCursor
}
# Establish Db connectiona and error handling
def get_db_connection():
    try:
        return pymysql.connect(**DB_CONFIG)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
#Define end point @/users", choose db conn and send the mysql query and close connection
@app.get("/users")
def get_all_users():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, email, role FROM users;")
            users = cursor.fetchall()
            return {"status": "success", "data": users} #print json response
    finally:
        connection.close()
#Define end point @/users/{user_id}", choose db conn and send the mysql query and close connection
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, email, role FROM users WHERE id = %s;", (user_id,))
            user = cursor.fetchone()
            if not user:
                raise HTTPException(status_code=404, detail="User not found") #error handle
            return {"status": "success", "data": user} #print json response
    finally:
        connection.close()
#Define end point @/users/name/{user_name}", choose db conn and send the mysql query and close connection		
@app.get("/users/name/{user_name}")
def get_user_by_name(user_name: str):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, email, role FROM users WHERE name =  %s;", (user_name,))
            user = cursor.fetchone()
            if not user:
                raise HTTPException(status_code=404, detail="User not found") #error handle
            return {"status": "success", "data": user} #print json response
    finally:
        connection.close()
