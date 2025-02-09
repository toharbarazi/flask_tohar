from flask import Flask, request, jsonify

app = Flask(__name__)

# שמירה על רשימת משתמשים
users = []

# GET request להחזרת כל המשתמשים
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST request להוספת משתמש חדש
@app.route('/users', methods=['POST'])
def add_user():
    user = request.get_json()
    users.append(user)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(debug=True)

