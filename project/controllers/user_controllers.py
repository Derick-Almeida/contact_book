from flask import request
from project.services import UserServices, session
from project.utils import verify_token_middleware


class UserControllers:
    def create_user() -> dict:
        return UserServices.create_user(request.get_json())

    def retrieve_user(id: str) -> list[dict]:
        check_token = verify_token_middleware()

        if check_token[0] is True:
            return UserServices.retrieve_user(id)

        return check_token

    def update_user(id: str) -> dict:
        check_token = verify_token_middleware()

        if check_token[0] is True:
            return UserServices.update_user(id, request.get_json())

        return check_token

    def delete_user(id: str) -> None:
        check_token = verify_token_middleware()

        if check_token[0] is True:
            return UserServices.delete_user(id)

        return check_token

    def user_login():
        return session(request.get_json())
