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

# הוספת endpoint נוסף עבור ה-GET request הראשי (למנוע 404 בבדיקות)
@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

