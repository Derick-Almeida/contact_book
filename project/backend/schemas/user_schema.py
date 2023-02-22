from jsonschema import Draft7Validator

schema = {
    "type": "object",
    "required": ["name", "password", "email", "phone"],
    "properties": {
        "name": {
            "type": "string",
            "minLength": 3,
            "maxLength": 255,
        },
        "email": {
            "type": "string",
            "minLength": 10,
            "maxLength": 255,
        },
        "phone": {
            "type": "string",
            "minLength": 9,
            "maxLength": 15,
        },
        "password": {
            "type": "string",
            "minLength": 6,
            "maxLength": 255,
        },
    },
}

user_validator = Draft7Validator(schema)
