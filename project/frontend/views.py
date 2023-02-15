from flask import render_template


def home():
    return render_template("index.html")


def login():
    return render_template("login.html")


def register():
    return render_template("register.html")


def dashboard():
    return "dashboard"
