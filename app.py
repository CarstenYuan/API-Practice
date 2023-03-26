from flask import Flask, request, jsonify
import mysql.connector


# Use local MySQL DB here
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='practice'
)

cursor = db.cursor()
# Create table if not exists
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS account (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(32) NOT NULL UNIQUE,
    password VARCHAR(32) NOT NULL
    )
    """
)

app = Flask(__name__)


@app.route('/create-account', methods=['POST'])
def create_account():
    # request_data = {'username': 'testuser', 'password': 'Test1234'}
    request_data = request.get_json()

    # Username already exists
    cursor.execute("SELECT * FROM account WHERE username = %s", (request_data['username'], ))
    user = cursor.fetchone()
    if user:
        return jsonify({
            'success': False,
            'reason': 'Username already exists.'
        }), 409

    # Username too short
    if len(request_data['username']) < 3:
        return jsonify({
            'success': False,
            'reason': 'Username too short.'
        }), 400

    # Username too long
    if len(request_data['username']) > 32:
        return jsonify({
            'success': False,
            'reason': 'Username too long.'
        }), 400

    # Password too short
    if len(request_data['password']) < 8:
        return jsonify({
            'success': False,
            'reason': 'Password too short.'
        }), 400

    # Password too long
    if len(request_data['password']) > 32:
        return jsonify({
            'success': False,
            'reason': 'Password too long.'
        }), 400

    # If contain at least 1 lowercase character
    if not any(char.islower() for char in request_data['password']):
        return jsonify({
            'success': False,
            'reason': 'Must contain at least 1 lowercase character.'
        }), 400

    # If contain at least 1 uppercase character
    if not any(char.isupper() for char in request_data['password']):
        return jsonify({
            'success': False,
            'reason': 'Must contain at least 1 uppercase character.'
        }), 400

    # If contain at least 1 digit
    if not any(char.isdigit() for char in request_data['password']):
        return jsonify({
            'success': False,
            'reason': 'Must contain at least 1 digit.'
        }), 400

    # Insert new username and password into the account table
    cursor.execute("INSERT INTO account (username, password) "
                   "VALUES (%s, %s)", (request_data['username'], request_data['password']))
    db.commit()

    return jsonify({
        'success': True
    }), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
