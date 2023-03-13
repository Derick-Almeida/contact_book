from project.repository import GetRepository
from project.utils import ValidateFields, ValidateUpdateFields, ValidateUnique
from project.schemas import user_validator, user_patch_validator
from datetime import datetime
import uuid
from passlib.hash import pbkdf2_sha256


class UserServices:
    def create_user(data: dict) -> dict:
        check = ValidateFields(data, user_validator)
        is_unique = ValidateUnique(data)

        if check.is_valid():
            data = check.clean_data()

            if is_unique.email("users"):
                return is_unique.email("users")

            if is_unique.phone("users"):
                return is_unique.phone("users")

            data["password"] = pbkdf2_sha256.hash(data.get("password"))

            data["_id"] = str(uuid.uuid4())
            data["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            user, status = GetRepository("users").create(data)
            user_data = user.get_json()
            user_data.pop("password")

            return user_data, status
        else:
            return check.errors(), 400

    def retrieve_user(id: str) -> dict:
        user, status = GetRepository("users").retrieve(id)
        user_data = user.get_json()

        if user_data.get("password"):
            user_data.pop("password")

        all_contacts, _ = GetRepository("contacts").list()
        contacts = [
            contact
            for contact in all_contacts.get_json()
            if contact["user"] == user_data["_id"]
        ]

        user_data["contacts"] = contacts

        return user_data, status

    def update_user(id: str, data: dict) -> dict:
        check = ValidateUpdateFields(data, user_patch_validator)
        is_unique = ValidateUnique(data)

        if check.is_valid():
            data = check.clean_data()

            if data.get("email"):
                if is_unique.email():
                    return is_unique.email()

            if data.get("phone"):
                if is_unique.phone():
                    return is_unique.phone()

            if data.get("password"):
                data["password"] = pbkdf2_sha256.hash(data.get("password"))

            data["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            user, status = GetRepository("users").update(data, id)
            user_data = user.get_json()
            if user_data.get("password"):
                user_data.pop("password")

            return user_data, status
        else:
            return check.errors()

    def delete_user(id: str) -> None:
        return GetRepository("users").delete(id)
