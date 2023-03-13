from jsonschema import Draft7Validator

schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "minLength": 3,
            "maxLength": 255,
        },
        "email": {
            "type": "string",
            "pattern": "^\\w+([\\.-]?\\w+)*@\\w+([\\.-]?\\w+)*(\\.\\w{2,3})+$",
            "minLength": 5,
            "maxLength": 255,
        },
        "phone": {
            "type": "string",
            "minLength": 9,
            "maxLength": 15,
        },
    },
}

contact_validator = Draft7Validator(
    {
        **schema,
        "required": ["name", "email", "phone"],
    }
)

contact_patch_validator = Draft7Validator(schema)
