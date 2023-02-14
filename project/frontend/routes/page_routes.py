from flask import Flask
from project.frontend import views


def page_routes(app: Flask):
    app.route("/")(views.home)
    app.route("/login")(views.login)
    app.route("/register")(views.register)
    app.route("/dashboard")(views.dashboard)
