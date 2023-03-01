from flask import jsonify, request
from jwt import decode, exceptions
import os


def validate_token(token: str, output: bool = False):
    try:
        if output:
            return decode(token, os.getenv("SECRET_KEY"), ["HS256"])
        decode(token, os.getenv("SECRET_KEY"), ["HS256"])

    except exceptions.DecodeError:
        return jsonify({"message": "Invalid Token"}), 401

    except exceptions.ExpiredSignatureError:
        return jsonify({"message": "Token Expired"}), 401


def verify_token_middleware():
    token = request.headers["Authorization"].split(" ")[-1]
    return validate_token(token)
