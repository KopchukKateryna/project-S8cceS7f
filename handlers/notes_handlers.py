from tabulate import tabulate
from classes import NotesBook, Note


def handle_errors(func):
    """
    Decorator to handle errors and provide user-friendly messages.

    Args:
        func (function): The function to wrap with error handling.

    Returns:
        function: The wrapped function with error handling.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: {str(e)}"
        except ValueError as e:
            return f"Invalid input: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    return wrapper


@handle_errors
def add_note(notebook: NotesBook):
    """
    Adds a new note to the notes list.

    Args:
        notebook (NotesBook): The notes list.

    Returns:
        str: Message indicating that the note has been added or an error occurred.
    """
    name = input("Enter note name: ")
    if name:
        text = input("Enter note text: ")
        if text:
            note = notebook.find(name)
            if note is None:
                note = Note(name, text)
                notebook.add_note(note)
                return "Note added."
            else:
                return f"Note with name '{name}' already exists."
        else:
            return "Text cannot be empty."
    else:
        return "Name cannot be empty."


@handle_errors
def show_all_notes(notebook: NotesBook):
    """
    Shows all notes in the list.

    Args:
        notebook (NotesBook): The notes list.

    Returns:
        str: Formatted string with all notes or an error message.
    """
    if not notebook.data:
        return "No notes found."

    headers = ["Note Name", "Text"]
    rows = [(note.name.value, note.text.value) for note in notebook.data.values()]
    return tabulate(rows, headers, tablefmt="grid", stralign="left")


@handle_errors
def add_tag(args, notebook: NotesBook):
    note_name, tag, *_ = args 
    return notebook.add_tag(note_name, tag)

@handle_errors
def add_tags(args, notebook: NotesBook):
    note_name, *tags = args 
    return notebook.add_tags(note_name, tags)

@handle_errors
def edit_tag(args, notebook: NotesBook):
    note_name, old_tag, new_tag, *_ = args 
    return notebook.edit_tag(note_name, old_tag, new_tag)

@handle_errors
def remove_tag(args, notebook: NotesBook):
    note_name, tag, *_ = args 
    return notebook.remove_tag(note_name, tag)

@handle_errors
def remove_tags(args, notebook: NotesBook):
    note_name, *tags = args 
    return notebook.remove_tags(note_name, tags)

@handle_errors
def notes_by_tag(args, notebook: NotesBook):
    tag, *_ = args
    return notebook.get_notes_by_tag(tag)

@handle_errors
def all_tags_by_note_name(args, notebook: NotesBook):
    note_name, *_ = args 
    return notebook.all_tags_by_note_name(note_name)

@handle_errors
def all_tags(notebook: NotesBook):
    return notebook.all_tags()
