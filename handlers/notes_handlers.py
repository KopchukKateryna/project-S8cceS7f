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
    return tabulate(rows, headers, tablefmt="mixed_grid", stralign="left")


@handle_errors
def find_note(notebook: NotesBook):
    """Finds and returns notes by searching for a keyword in their names from the notebook.
    Handles user input directly.
    Args:
        notebook (NotesBook): The notebook to search in.
    Returns:
        str: The notes that match the search, or a message if no matches are found."""

    while True:
        note_name = input("Enter the note name or keyword: ").strip().lower()
        if note_name:
            matching_notes = [
                note for note in notebook.data.values()
                if note_name in str(note.name).lower()
            ]
            if matching_notes:
                headers = ["Note Name", "Text"]
                rows = [(str(note.name), str(note.text)) for note in matching_notes]
                return tabulate(rows, headers, tablefmt="mixed_grid", stralign="left")
            else:
                return "No notes found matching that keyword."
        if note_name == "no":
            break


@handle_errors
def edit_note(notebook: NotesBook):
    """
    Edits the text of an existing note in the notebook.

    Prompts the user to enter the name of the note they wish to edit.
    If the note is found, it asks for the new text and updates the note.
    If the note is not found, or if the new text is empty, an appropriate
    message is returned.

    Args:
        notebook (NotesBook): The notebook instance containing notes.

    Returns:
        str: The updated note if the operation is successful, or an error message
            if the note is not found or if the new text is empty.
    """

    note_name = input("Enter the note name: ").strip()
    if note_name:
        note = notebook.find(note_name)
        if note:
            new_text = input("Enter the new text: ").strip()
            if new_text:  # Ensure the new text is not empty
                note.edit_note(new_text)
                return note
            else:
                return "Text could not be empty. Please enter the new text."
        else:
            return "Note not found."
    else:
        return "Please enter the name."


def remove_note(notebook: NotesBook):
    note_name = input("Enter the note name: ").strip()
    if note_name:
        note = notebook.find(note_name)
        if note:
            notebook.delete(note_name)
            return f"Note {note_name} has been deleted"

        if note_name == "all":
            notebook.data.clear()
            return "All notes have been deleted"
        else:
            return "Note not found."
    else:
        return "Please enter the name."
