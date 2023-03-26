from flask import Flask, request
import mysql.connector


# Use local MySQL DB here
db = mysql.connector.connect(
    host='localhost',
    user='admin',
    password='admin',
    database='practice'
)

cursor = db.cursor()
# Create table if not exists
cursor.execute(
    """
    CREATE TABLE IF NOT EXIST account (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(32) NOT NULL UNIQUE,
    password VARCHAR(32) NOT NULL,
    )
    """
)

app = Flask(__name__)


@app.route('/create-account', methods=['POST'])
def create_account():
    # request_data = {'username': 'testuser', 'password': 'Test1234'}
    request_data = request.get_json()

    # Insert new username and password into the account table
    cursor.execute("INSERT INTO account (username, password) "
                   "VALUES (%s, %s)", (request_data['username'], request_data['password']))