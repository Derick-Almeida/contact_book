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
        query = self.collection.insert_one(data)
        obj = self.collection.find_one({"_id": query.inserted_id})

        return jsonify(obj), 201

    def list(self) -> list[dict]:
        query = list(self.collection.find())

        return jsonify(query), 200

    def retrieve(self, id: str) -> dict:
        query = self.collection.find_one({"_id": id})

        if not bool(query):
            return jsonify({"message": "Not found."}), 404

        return jsonify(query), 200

    def update(self, data: dict, id: str) -> dict:
        query = self.collection.find_one_and_update(
            {"_id": id}, {"$set": data}, return_document=True
        )

        if not bool(query):
            return jsonify({"message": "Not found."}), 404

        return jsonify(query), 200

    def delete(self, id: str) -> None:
        query = self.collection.find_one_and_delete({"_id": id})

        if not bool(query):
            return jsonify({"message": "Not found."}), 404

        return jsonify(), 204

    def check_unique(self, *args) -> dict:
        query = self.collection.find_one(*args)

        if not bool(query):
            return False

        return True

    def find_one(self, *args) -> dict:
        query = self.collection.find_one(*args)

        return query
