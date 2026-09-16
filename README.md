# ======== Kavee's API=============####
# pyApiForMysqlQuery
Api designed using python to query details from mysl db
Steps to implement
1. Clone the project to your workspace
git clone git_url
2. create mysql db and table. load data use below sample or you can have your own specific tables(py scripts need to adjust according to your own table structure)
 mysql -u root -p
Run the following SQL commands to set up your database, table, and test record:
# Create table db
CREATE DATABASE company_db;
USE company_db;
# create table and load data
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL
);

INSERT INTO users (name, email, role) 
VALUES ('Alice Smith', 'alice@example.com', 'DevOps Engineer');

EXIT;

3. Create Python Virtual Environment & Install Dependencies:Isolate libraries using FastAPI, Uvicorn, and PyMySQL.
Open your terminal and run:

# go to project directory
cd pyApiForMysqlQuery
# install venv
apt install python3.12-venv
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install FastAPI, Uvicorn (web server), and PyMySQL
pip install fastapi uvicorn pymysql
# install dot .env to safely pass credentials
pip install python-dotenv

4. Modify the database connection details inside the .env[project root directory] 
# Add .env file
vim .env

DB_HOST=localhost or ip
DB_USER=user
DB_PASSWORD=password
DB_NAME=company_db

# Note: to prevent .env credentials commit to Git repo, add below lines to .gitignore file

vim .gitignore
.env
__pycache__/
*.pyc
main.py-v1


5. Run the app
# open a screen
screen -S pyapi
# go to project directory and activate venv here
cd pyApiForMysqlQuery
source venv/bin/activate

# run application
uvicorn main:app --reload --port 8000
# Exit Screen
ctrl+A+D to exit screen
6. Test the API(you can use curl or postman)

curl http://localhost:8000/users
curl http://localhost:8000/users/{id}
curl http://localhost:8000/users/name/{user_name}

