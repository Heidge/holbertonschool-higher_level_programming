from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
auth = HTTPBasicAuth()
#va permettre d'utiliser le décorateur auth.<nom>
app.config["JWT_SECRET_KEY"] = "Asejot1204-"
jwt = JWTManager(app)


users = {
      "user1": {"username": "user1", "password": generate_password_hash("user1password"), "role": "user"},
      "admin1": {"username": "admin1", "password": generate_password_hash("admin1password"), "role": "admin"}
  }

@auth.verify_password
#lorsqu'il y a un décorateur auth.login_required, cette fonction est appelée automatiquement
def verify_password(username, password):
    if username in users:
        if check_password_hash(users[username]["password"], password): 
        #On parcourt un dictionaire qui contient des dictionnaires (imbrication)
            return username
    return False

@app.route("/")
def home():
    """
    Home route

    Returns:
        string: simple welcome message for the homepage
    """
    return jsonify("Welcome to the Flask API!")

@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify("Basic Auth: Access Granted"), 200

@app.route("/login", methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 201

@app.route("/jwt-protected")
@jwt_required
def jwt_protected():
    return "JWT Auth: Access Granted", 200


if __name__ == "__main__": app.run(None, 5007)
