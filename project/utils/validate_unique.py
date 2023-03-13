from flask import jsonify
from project.repository import GetRepository


class ValidateUnique:
    def __init__(self, data: dict) -> None:
        self.data = data

    def email(self, collection: str) -> dict | None:
        check_email = GetRepository(collection).check_unique(
            {"email": self.data["email"]}
        )
        if check_email:
            return jsonify({"email": "Email already exists."}), 400

    def phone(self, collection: str) -> dict | None:
        check_phone = GetRepository(collection).check_unique(
            {"phone": self.data["phone"]}
        )
        if check_phone:
            return jsonify({"phone": "Phone already exists."}), 400
