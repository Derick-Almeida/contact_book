from flask import Flask
from project.routes.user_routes import user_routes
from project.routes.contact_routes import contact_routes


def init_app(app: Flask):
    user_routes(app)
    contact_routes(app)
