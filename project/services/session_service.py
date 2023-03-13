from flask import jsonify
from jwt import encode
from datetime import datetime, timedelta
from project.repository import GetRepository
from passlib.hash import pbkdf2_sha256
import os


def expire_data(hours: int):
    now = datetime.now()
    new_date = now + timedelta(hours=hours)

    return new_date


def session(data: dict) -> dict:
    user = GetRepository("users").find_one({"email": data.get("email")})

    if not user:
        return jsonify({"message": "Invalid email or password"}), 403

    check_password = pbkdf2_sha256.verify(data.get("password"), user.get("password"))

    if not check_password:
        return jsonify({"message": "Invalid email or password"}), 403

    token = encode(
        payload={"user_id": user["_id"], "exp": expire_data(24)},
        key=os.getenv("SECRET_KEY"),
    )
    return jsonify({"token": token})
