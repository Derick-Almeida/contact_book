from flask import jsonify
from project.backend.services import UserServices


class UserControllers:
    def create_user() -> dict:
        ...

    def list_users() -> list[dict]:
        user_list = list(UserServices.list_users())
        response = jsonify(user_list)

        return response, 200

    def retrieve_user(id: str) -> list[dict]:
        user = UserServices.retrieve_user(id)
        response = jsonify(user)

        return response, 200

    def update_user(id: str) -> dict:
        ...

    def delete_user(id: str) -> None:
        UserServices.delete_user(id)

        return jsonify(), 204
