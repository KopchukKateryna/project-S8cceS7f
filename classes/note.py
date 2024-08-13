"""class Note"""

from classes.field import Field


class Note:
    """
    A class representing a note with a name and text.

    Attributes:
        name (Field): The name of the note.
        text (Field): The text content of the note.
    """

    def __init__(self, name, text=""):
        """
        Initializes a Note instance with a name and optional text.

        Args:
            name (str): The name of the note.
            text (str, optional): The text content of the note. Defaults to empty string.
        """
        self.text = Field(text)
        self.name = Field(name)

    def __str__(self):
        """
        Returns a string representation of the note.

        Returns:
            str: A formatted string with the note's name and text.
        """
        return f"Note: {self.name.value}, Text: {self.text.value}"
