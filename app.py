from flask import Flask
from project.backend import routes as b_rutes
from project.frontend import routes as f_routes


def create_app():
    app = Flask(
        __name__,
        template_folder="./project/frontend/templates",
        static_folder="./project/frontend/static",
    )

    b_rutes.init_app(app)
    f_routes.init_app(app)

    return app


if __name__ == "__main__":
    create_app().run()
