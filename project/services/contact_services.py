from project.repository import GetRepository
from project.utils import ValidateFields, ValidateUnique
from project.schemas import contact_validator, contact_patch_validator
from datetime import datetime
from flask import jsonify
import uuid


class ContactServices:
    def create_contact(user_id: str, data: dict) -> dict:
        check = ValidateFields(data, contact_validator)
        is_unique = ValidateUnique(data)

        if check.is_valid():
            data = check.clean_data()

            if is_unique.email("contacts"):
                return is_unique.email("contacts")

            if is_unique.phone("contacts"):
                return is_unique.phone("contacts")

            data["_id"] = str(uuid.uuid4())
            data["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data["user"] = user_id

            return GetRepository("contacts").create(data)
        else:
            return check.errors(), 400

    def list_contact(user_id: str) -> list[dict]:
        all_contacts, status = GetRepository("contacts").list()
        contacts = [
            contact for contact in all_contacts.get_json() if contact["user"] == user_id
        ]

        return contacts, status

    def retrieve_contact(user_id: str, id: str) -> dict:
        contact, status = GetRepository("contacts").retrieve(id)

        if status == 200 and contact.get_json()["user"] == user_id:
            return contact, status
        else:
            return jsonify({"message": "Not found."}), 404

    def update_contact(user_id: str, id: str, data: dict) -> dict:
        contact, status = GetRepository("contacts").retrieve(id)

        if status == 200 and contact.get_json()["user"] == user_id:
            check = ValidateFields(data, contact_patch_validator)
            is_unique = ValidateUnique(data)

            if check.is_valid():
                data = check.clean_data()

                if data.get("email"):
                    if is_unique.email("contacts"):
                        return is_unique.email("contacts")

                if data.get("phone"):
                    if is_unique.phone("contacts"):
                        return is_unique.phone("contacts")

                data["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                return GetRepository("contacts").update(data, id)
            else:
                return check.errors(), 400

        return jsonify({"message": "Not found."}), 404

    def delete_contact(user_id: str, id: str) -> None:
        contact, status = GetRepository("contacts").retrieve(id)

        if status == 200 and contact.get_json()["user"] == user_id:
            return GetRepository("contacts").delete(id)

        return jsonify({"message": "Not found."}), 404
