from tabulate import tabulate
from classes import NotesBook, Note


def add_note(args, book: NotesBook):
    """Adds a new note to the notes list.

    Args:
        args (list): contains name and text
        book (class): notes list

    Returns:
        str: message that the note has been added or updated
    """
    name, text, *_ = args
    note = book.find(name)
    if note is None:
        note = Note(name, text)
        book.add_note(note)
        return "Note added."
    else:
        return f"Note with name '{name}' already exists."


def show_all_notes(book: NotesBook):
    """Shows all notes in the list.

    Args:
        book (NotesBook): notes list

    Returns:
        str: formatted string with all notes
    """
    if not book.data:
        return "No notes found."

    headers = ["Note Name", "Text"]
    rows = [(note.name.value, note.text) for note in book.data.values()]
    return tabulate(rows, headers, tablefmt="grid", stralign="left")
