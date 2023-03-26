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