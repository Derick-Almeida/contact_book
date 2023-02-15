from flask import jsonify
from flask_pymongo import pymongo
import os


class GetRepository:
    client = (
        pymongo.MongoClient(os.getenv("DATABASE_URL"))
        if os.getenv("PYTHON_ENV") == "production"
        else pymongo.MongoClient(host="localhost", port=27017)
    )
    db = client[os.getenv("DB_NAME")]

    def __init__(self, collection: str) -> None:
        self.collection = self.db[collection]

    def create(self, data: dict) -> dict:
        ...

    def list(self) -> list[dict]:
        return self.collection.find()

    def retrieve(self, id: str) -> dict:
        return self.collection.find_one({"_id": id})

    def update(self, data: dict, id: str) -> dict:
        ...

    def delete(self, id: str) -> None:
        self.collection.find_one_and_delete({"_id": id})

        return None
