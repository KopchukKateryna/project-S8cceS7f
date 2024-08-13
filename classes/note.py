from classes.name import Name
from classes import Record


class Note(Record):
    def __init__(self, name, text=""):
        self.name = Name(name)
        self.text = text

    def add_note_text(self, text: str):
        self.text = text

    def __str__(self):
        return f"Note: {self.name.value}, Text: {self.text}"
