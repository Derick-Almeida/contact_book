from project.services import ContactServices
from project.utils import verify_token_middleware
from flask import request


class ContactController:
    def create_contact() -> dict:
        check_token = verify_token_middleware()

        if check_token[0] is True:
            user_id = check_token[-1]["user_id"]

            return ContactServices.create_contact(user_id, request.get_json())

        return check_token

    def list_contacts() -> list[dict]:
        check_token = verify_token_middleware()

        if check_token[0] is True:
            user_id = check_token[-1]["user_id"]

            return ContactServices.list_contacts(user_id)

        return check_token

    def retrieve_contact(id: str) -> dict:
        check_token = verify_token_middleware()

        if check_token[0] is True:
            user_id = check_token[-1]["user_id"]

            return ContactServices.retrieve_contact(user_id, id)

        return check_token

    def update_contact(id: str) -> dict:
        check_token = verify_token_middleware()

        if check_token[0] is True:
            user_id = check_token[-1]["user_id"]

            return ContactServices.update_contact(user_id, id, request.get_json())

        return check_token

    def delete_contact(id: str) -> None:
        check_token = verify_token_middleware()

        if check_token[0] is True:
            user_id = check_token[-1]["user_id"]

            return ContactServices.delete_contact(user_id, id)

        return check_token
