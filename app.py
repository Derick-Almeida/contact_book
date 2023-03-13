from flask import Flask
from project import routes


def create_app():
    app = Flask(__name__)

    routes.init_app(app)

    return app


if __name__ == "__main__":
    create_app().run()
