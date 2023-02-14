from flask import Flask
from .page_routes import page_routes


def init_app(app: Flask):
    page_routes(app)
