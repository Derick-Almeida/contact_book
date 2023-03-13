from flask import Flask
from project.controllers import ContactController


def contact_routes(app: Flask):
    app.post("/api/contacts/")(ContactController.create_contact)
    app.get("/api/contacts/")(ContactController.list_contacts)
    app.get("/api/contacts/<id>")(ContactController.retrieve_contact)
    app.patch("/api/contacts/<id>")(ContactController.update_contact)
    app.delete("/api/contacts/<id>")(ContactController.delete_contact)
