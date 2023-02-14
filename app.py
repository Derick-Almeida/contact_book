from flask import Flask
from project.frontend import routes


def create_app():
    app = Flask(
        __name__,
        template_folder="./project/frontend/templates",
        static_folder="./project/frontend/static",
    )

    routes.init_app(app)

    return app


if __name__ == "__main__":
    create_app().run()
