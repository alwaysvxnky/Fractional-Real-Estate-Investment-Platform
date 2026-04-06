from flask import Blueprint, request, jsonify
from utils.db import get_db
from extensions import bcrypt

auth_bp = Blueprint("auth", __name__)

# -------- REGISTER --------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Missing fields"}), 400

    hashed = bcrypt.generate_password_hash(password).decode("utf-8")

    conn = get_db()
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed)
        )
        conn.commit()
        return jsonify({"msg": "User created"})
    except:
        return jsonify({"msg": "User already exists"})
    finally:
        conn.close()


# -------- LOGIN --------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    conn = get_db()
    c = conn.cursor()

    user = c.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    ).fetchone()

    conn.close()

    if user and bcrypt.check_password_hash(user[2], password):
        return jsonify({"msg": "Login success"})
    else:
        return jsonify({"msg": "Invalid credentials"}), 401