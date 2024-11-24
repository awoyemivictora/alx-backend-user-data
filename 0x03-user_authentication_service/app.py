#!/usr/bin/env python3
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """
    POST /users endpoint to register a new user.
    Expects 'email' and 'password' in form data.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        # Attempt to register the user
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        # If the email is already registered
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
