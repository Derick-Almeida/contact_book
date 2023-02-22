from flask import request
from project.backend.services import UserServices


class UserControllers:
    def create_user() -> dict:
        return UserServices.create_user(request.get_json())

    def list_users() -> list[dict]:
        return UserServices.list_users()

    def retrieve_user(id: str) -> list[dict]:
        return UserServices.retrieve_user(id)

    def update_user(id: str) -> dict:
        return UserServices.update_user(id, request.get_json())

    def delete_user(id: str) -> None:
        return UserServices.delete_user(id)
