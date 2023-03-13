from flask import jsonify, request
from jwt import decode, exceptions
import os


def validate_token(token: str):
    try:
        decoded = decode(token, key=os.getenv("SECRET_KEY"), algorithms=["HS256"])
        return (True, decoded)

    except exceptions.DecodeError:
        return jsonify({"message": "Invalid Token"}), 401

    except exceptions.ExpiredSignatureError:
        return jsonify({"message": "Token Expired"}), 401


def verify_token_middleware():
    try:
        token = request.headers["Authorization"].split(" ")[-1]
        return validate_token(token)
    except KeyError:
        return jsonify({"message": "Missing Token"}), 401
