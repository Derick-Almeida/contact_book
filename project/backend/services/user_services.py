from project.backend.repository import GetRepository


class UserServices:
    def create_user() -> dict:
        ...

    def list_users() -> list[dict]:
        user_list = GetRepository("users").list()

        return user_list

    def retrieve_user(id: str) -> list[dict]:
        user = GetRepository("users").retrieve(id)

        return user

    def update_user(id: str) -> dict:
        ...

    def delete_user(id: str) -> None:
        GetRepository("users").delete(id)

        return None
