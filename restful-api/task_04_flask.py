from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """
    Home route

    Returns:
        string: simple welcome message for the homepage
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def list_users():
    """_summary_

    Returns:
        json: json object with list appearence of all users registered in the API
    """
    usernames = []
    for username in users.keys():
        usernames.append(username)
    return jsonify(usernames)

@app.route("/status")
def status():
    """
    Status of the api

    Returns:
        string: return an OK if API is launched 
    """
    return "OK"

@app.route("/users/<username>")
def username(username):
    """
    Return data for a spiecific user with username specified in parameter

    Args:
        username (string): the username of the user data wanted

    Returns:
        json: retrieves json response of data or error message with 404 code if failed
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404
        
@app.route("/add_user", methods=['POST'])
def add_user():
    """
    Function that manage post data for user

    Returns:
        json: confirmation that user is added with data and 201 code confirmation also or error message with 400 code
    """
    user_data = request.get_json()
    if "username" not in user_data:
         return jsonify({"error": "Username is required"}), 400
    else:     
        users[user_data["username"]] = {
            "username": user_data["username"],
            "name": user_data["name"],
            "age": user_data["age"],
            "city": user_data["city"]
        }


    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__": app.run(None, 5000)
