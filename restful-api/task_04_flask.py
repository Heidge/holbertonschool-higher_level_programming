from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}, 
         "john": {"name": "John", "age": 30, "city": "New York"}}

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
    users[user_data["username"]] = {
        "name": user_data["name"],
        "age": user_data["age"],
        "city": user_data["city"]
    }


    return jsonify({
        "message": "User added",
        "user": {
            "username": user_data["username"],
            "name": user_data["name"],
            "age": user_data["age"],
            "city": user_data["city"]
        }
    })

if __name__ == "__main__": app.run(None, 5000)
