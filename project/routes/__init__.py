from flask import Flask
from project.routes.user_routes import user_routes


def init_app(app: Flask):
    user_routes(app)
