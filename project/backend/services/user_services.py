from project.backend.repository import GetRepository
from project.backend.utils import ValidateFields
from datetime import datetime
import uuid


class UserServices:
    def create_user(data: dict) -> dict:
        check = ValidateFields(data)

        if check.is_valid():
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

    def update_user(id: str) -> dict:
        ...

    def delete_user(id: str) -> None:
        return GetRepository("users").delete(id)
