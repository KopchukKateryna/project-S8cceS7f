"""A class for storing a contact's birthday."""

from datetime import datetime
from classes.field import Field


class Birthday(Field):
    """
    A class for storing a contact's birthday.

    Inherits from Field. Validates that the birthday is in the format YYYY.MM.DD and converts
    the string representation to a datetime object.

    Method:
        __init__(self, value: str) - Initializes the birthday with a validated date.
    """
    def __init__(self, value: str):
        try:
            birthday = datetime.strptime(value, "%Y.%m.%d")
            super().__init__(birthday)
        except ValueError as exc:
            raise ValueError("Invalid date format. Use YYYY.MM.DD") from exc

    def __str__(self):
        return f'{self.value.strftime("%Y.%m.%d")}'
