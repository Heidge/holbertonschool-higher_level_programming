from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def list_users():
    usernames = []
    for username in users.keys():
        usernames.append(username)
    return jsonify(usernames)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def username(username):
        if username in users:
            return jsonify(users[username])
        else:
            return jsonify({"error": "User not found"})
        
@app.route("/add_user", methods=['POST'])
def add_user():
    user_data = request.get_json()
    if "username" not in user_data:
         return jsonify({"error": "Username is required"}), 400
    else:     
        users[user_data["username"]] = {
            "name": user_data["name"],
            "age": user_data["age"],
            "city": user_data["city"]
        }


    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__": app.run(None, 5000)
