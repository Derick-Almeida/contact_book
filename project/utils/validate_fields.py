from project.schemas import user_validator, user_patch_validator


class ValidateFields:
    def __init__(self, data: dict, validator=user_validator) -> None:
        self.data = data
        self.validator = validator

    def is_valid(self) -> bool:
        if self.validator.is_valid(self.data):
            return True
        else:
            return False

    def clean_data(self) -> dict:
        new_data = dict(**self.data)
        data_fields = self.data.keys()
        schema_fields = self.validator.schema["properties"].keys()

        for field in data_fields:
            if field not in schema_fields:
                new_data.pop(field)

        return new_data

    def errors(self) -> dict:
        errors = {}

        for err in list(self.validator.iter_errors(self.data)):
            if err.validator is "required":
                fields = err.validator_value

                for field in fields:
                    if field in err.message:
                        errors[field] = "This field is required."

            if err.validator is "minLength":
                field = err.json_path[2:]
                errors[
                    field
                ] = f"The field must contain at least {err.validator_value} characters"

            if err.validator is "maxLength":
                field = err.json_path[2:]
                errors[
                    field
                ] = f"The field must have a maximum of {err.validator_value} characters"

        return errors


class ValidateUpdateFields(ValidateFields):
    def __init__(self, data: dict, validator=user_patch_validator) -> None:
        self.data = data
        self.validator = validator
