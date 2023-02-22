from project.backend.repository import GetRepository
from project.backend.utils import ValidateFields, ValidateUpdateFields, ValidateUnique
from datetime import datetime
import uuid


class UserServices:
    def create_user(data: dict) -> dict:
        check = ValidateFields(data)
        is_unique = ValidateUnique(data)

        if check.is_valid():
            data = check.clean_data()

            if is_unique.email():
                return is_unique.email()

            if is_unique.phone():
                return is_unique.phone()

            data["_id"] = str(uuid.uuid4())
            data["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            user = GetRepository("users").create(data)

            return user
        else:
            return check.errors()

    def list_users() -> list[dict]:
        return GetRepository("users").list()

    def retrieve_user(id: str) -> list[dict]:
        return GetRepository("users").retrieve(id)

    def update_user(id: str, data: dict) -> dict:
        check = ValidateUpdateFields(data)
        is_unique = ValidateUnique(data)

        if check.is_valid():
            data = check.clean_data()

            if data.get("email"):
                if is_unique.email():
                    return is_unique.email()

            if data.get("phone"):
                if is_unique.phone():
                    return is_unique.phone()

            data["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            user = GetRepository("users").update(data, id)

            return user
        else:
            return check.errors()

    def delete_user(id: str) -> None:
        return GetRepository("users").delete(id)
