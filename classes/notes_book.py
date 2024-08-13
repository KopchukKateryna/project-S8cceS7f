from classes import AddressBook


class NotesBook(AddressBook):
    def __str__(self):
        lines = [str(note) for note in self.data.values()]
        return "\n".join(lines)

    def add_note(self, note):
        if note.name.value in self.data:
            raise KeyError(f"Note with name '{note.name.value}' already exists.")
        self.data[note.name.value] = note

    def find(self, name):
        return self.data.get(name, None)
