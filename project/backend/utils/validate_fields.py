from project.backend.schemas import user_validator


class ValidateFields:
    def __init__(self, data: dict) -> None:
        self.data = data

    def is_valid(self) -> bool:
        if user_validator.is_valid(self.data):
            return True
        else:
            return False

    def errors(self) -> dict:
        errors = {}

        for err in list(user_validator.iter_errors(self.data)):
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
