from flask import Flask
from project.backend.controllers import UserControllers


def user_routes(app: Flask):
    app.post("/api/users")(UserControllers.create_user)
    app.get("/api/users")(UserControllers.list_users)
    app.get("/api/users/<id>")(UserControllers.retrieve_user)
    app.patch("/api/users/<id>")(UserControllers.update_user)
    app.delete("/api/users/<id>")(UserControllers.delete_user)
