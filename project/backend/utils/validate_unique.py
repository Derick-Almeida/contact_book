from flask import jsonify
from project.backend.repository import GetRepository


class ValidateUnique:
    def __init__(self, data: dict) -> None:
        self.data = data

    def email(self) -> dict | None:
        check_email = GetRepository("users").check_unique({"email": self.data["email"]})
        if check_email:
            return jsonify({"message": "Email already exists."}), 400

    def phone(self) -> dict | None:
        check_phone = GetRepository("users").check_unique({"phone": self.data["phone"]})
        if check_phone:
            return jsonify({"message": "Phone already exists."}), 400
