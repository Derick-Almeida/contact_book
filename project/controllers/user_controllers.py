from flask import request
from project.services import UserServices, session
from project.utils import verify_token_middleware


class UserControllers:
    def create_user() -> dict:
        return UserServices.create_user(request.get_json())

    def retrieve_user(id: str) -> list[dict]:
        check_token = verify_token_middleware()

        if check_token is not None:
            return check_token

        return UserServices.retrieve_user(id)

    def update_user(id: str) -> dict:
        check_token = verify_token_middleware()

        if check_token is not None:
            return check_token

        return UserServices.update_user(id, request.get_json())

    def delete_user(id: str) -> None:
        check_token = verify_token_middleware()

        if check_token is not None:
            return check_token

        return UserServices.delete_user(id)

    def user_login():
        return session(request.get_json())
