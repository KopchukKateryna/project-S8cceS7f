from prompt_toolkit import prompt
from classes import NotesBook, Note
from constants import COMPLETER_FOR_NAME_TEXT
from helpers import bindings_for_name_text, table_show, custom_print, command_logger

headers = ["Note Name", "Text", "Tags"]
header = ["Tags"]


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
    custom_print(
        command_logger,
        "{msg}",
        space="top",
        level="info",
        msg=("cyan", "Please, enter the note name:"),
    )
    name = input(">> ").strip()
    if name:
        custom_print(
            command_logger,
            "{msg}",
            space="top",
            level="info",
            msg=("cyan", "Please, enter the note text:"),
        )
        text = input(">> ")
        if text:
            note = notebook.find(name)
            if note is None:
                note = Note(name, text)
                notebook.add_note(note)
                custom_print(
                    command_logger,
                    "{msg}",
                    space="top",
                    level="info",
                    msg=("green", "Note successfully added!"),
                )
            else:
                custom_print(
                    command_logger,
                    "Note with name {name} already exists.",
                    space="top",
                    level="warning",
                    name=("bright_cyan", name),
                )
        else:
            custom_print(
                command_logger,
                "Text cannot be empty.",
                space="top",
                level="warning",
            )
    else:
        custom_print(
            command_logger,
            "Name cannot be empty.",
            space="top",
            level="warning",
        )


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
        custom_print(
            command_logger,
            "No notes found.",
            space="top",
            level="warning",
        )

    rows = [
        (note.name.value, note.text.value, " ".join(note.tags))
        for note in notebook.data.values()
    ]
    print(table_show(headers, rows))


@handle_errors
def find_note(notebook: NotesBook):
    """Finds and returns notes by searching for a keyword in their
    names from the notebook.
    Handles user input directly.
    Args:
        notebook (NotesBook): The notebook to search in.
    Returns:
        str: The notes that match the search, or a message if no matches are found."""

    while True:
        custom_print(
            command_logger,
            "Please, enter the note name or keyword or {exit} to exit:",
            space="top",
            level="info",
            exit=("bright_magenta"),
        )
        note_name = input(">> ").strip()
        if note_name == "exit":
            break
        elif note_name:
            matching_notes = [
                note
                for note in notebook.data.values()
                if note_name.lower() in str(note.name).lower()
            ]
            if matching_notes:
                rows = [
                    (str(note.name), str(note.text), " ".join(note.tags))
                    for note in matching_notes
                ]
                print(table_show(headers, rows))
                return
            else:
                custom_print(
                    command_logger,
                    "No notes found matching that keyword.",
                    space="top",
                    level="warning",
                )
                return
        else:
            custom_print(
                command_logger,
                "Please, enter a note name or keyword.",
                space="top",
                level="warning",
            )


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
    custom_print(
        command_logger,
        "{msg}",
        space="top",
        level="info",
        msg=("cyan", "Please enter the name of the note you want to edit: "),
    )
    name = input(">> ").strip()
    note = notebook.find(name)
    if note:
        while True:
            custom_print(
                command_logger,
                "What do you want to change: ({name}/{text} or {exit} for go exit)",
                space="top",
                level="info",
                name="bright_magenta",
                text="bright_magenta",
                exit="magenta",
            )
            usr_chose = prompt(
                ">> ",
                completer=COMPLETER_FOR_NAME_TEXT,
                complete_while_typing=True,
                key_bindings=bindings_for_name_text,
                multiline=True,
            )
            if usr_chose == "name":
                while True:
                    custom_print(
                        command_logger,
                        "Please, type new name or {back} to go back: ",
                        space="top",
                        level="info",
                        back="magenta",
                    )
                    new_name = input(">> ").strip()
                    if new_name == "back":
                        break
                    elif new_name:
                        note.edit_name(new_name)
                        notebook.add_note(note)
                        notebook.delete(name)
                        custom_print(
                            command_logger,
                            "{msg}",
                            space="top",
                            level="info",
                            msg=("green", "Note successfully changed!"),
                        )
                        return
                    else:
                        custom_print(
                            command_logger,
                            "New note name cannot be empty.",
                            space="top",
                            level="warning",
                        )

            elif usr_chose == "text":
                while True:
                    custom_print(
                        command_logger,
                        "Please, type new text or {back} to go back: ",
                        space="top",
                        level="info",
                        back="magenta",
                    )
                    text = input(">> ").strip()
                    if text == "back":
                        break
                    elif text:
                        note.edit_note(text)
                        custom_print(
                            command_logger,
                            "{msg}",
                            space="top",
                            level="info",
                            msg=("green", "Note successfully changed!"),
                        )
                        return
                    else:
                        custom_print(
                            command_logger,
                            "New note text cannot be empty.",
                            space="top",
                            level="warning",
                        )

            elif usr_chose == "exit":
                custom_print(
                    command_logger,
                    "{msg}",
                    space="top",
                    level="warning",
                    msg=("bright_yellow", "Editing completed."),
                )
                return

            else:
                custom_print(
                    command_logger,
                    "Command not found. If you don't want to edit note type {exit}",
                    space="top",
                    level="warning",
                    exit="magenta",
                )
    else:
        custom_print(
            command_logger,
            "Note with name {name} haven't found!",
            space="top",
            level="warning",
            name=("magenta", name),
        )
        return


def remove_note(note_name: str, notebook: NotesBook):
    """
    Removes a note from the notebook.
    Prompts the user to enter the name of the note they wish to remove.
    If the note is found, it is removed from the notebook.
    If the note is not found, an appropriate message is returned.

    Args:
        note_name (str): The name of the note to remove.
        notebook (NotesBook): The notebook instance containing notes.

    Returns:
        str: message
    """
    note_name = note_name.strip().lower()
    if note_name:
        note = next((name for name in notebook.data if name.lower() == note_name), None)
        if note:
            notebook.delete(note)
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", "The note has been deleted!"),
            )
            return

        elif note_name == "all":
            notebook.data.clear()
            custom_print(
                command_logger,
                "{msg}",
                space="top",
                level="info",
                msg=("green", "All notes have been deleted!"),
            )
            return
        else:
            custom_print(
                command_logger,
                "Note with name {note_name} haven't found!",
                space="top",
                level="warning",
                note_name=("magenta", note_name),
            )
            return
    else:
        custom_print(
            command_logger,
            "Please enter {delete_note1} or {delete_note2}",
            space="top",
            level="warning",
            delete_note1=("magenta", "delete-note <note_name>"),
            delete_note2=("magenta", "delete-note all"),
        )
        return


@handle_errors
def add_tag(note, tag, notebook: NotesBook):
    """
    Adds a tag to a note in the notebook.

    Args:
        note (str): The name of the note to add the tag to.
        tag (str): The tag to add to the note.
        notebook (NotesBook): The notebook to add the tag to.

    Returns:
        None
    """
    return notebook.add_tag(note, tag)


@handle_errors
def add_tags(args, notebook: NotesBook):
    """
    Adds multiple tags to a note in the notebook.

    Args:
        args (tuple): A tuple containing the note name and a list of tags to add.
        notebook (NotesBook): The notebook to add the tags to.

    Returns:
        None
    """
    note_name, tags = args
    return notebook.add_tags(note_name, tags)


@handle_errors
def edit_tag(note, old_tag, new_tag, notebook: NotesBook):
    """
    Edits a tag on a note in the notebook.

    Args:
        note (str): The name of the note to edit the tag on.
        old_tag (str): The old tag to replace.
        new_tag (str): The new tag to replace the old tag with.
        notebook (NotesBook): The notebook to edit the tag in.

    Returns:
        None
    """
    return notebook.edit_tag(note, old_tag, new_tag)


@handle_errors
def remove_tag(note, tag, notebook: NotesBook):
    """
    Removes a tag from a note in the notebook.

    Args:
        note (str): The name of the note to remove the tag from.
        tag (str): The tag to remove from the note.
        notebook (NotesBook): The notebook to remove the tag from.

    Returns:
        None
    """
    return notebook.remove_tag(note, tag)


@handle_errors
def remove_tags(args, notebook: NotesBook):
    """
    Removes multiple tags from a note in the notebook.

    Args:
        args (tuple): A tuple containing the note name and a list of tags to remove.
        notebook (NotesBook): The notebook to remove the tags from.

    Returns:
        None
    """
    note_name, tags = args
    return notebook.remove_tags(note_name, tags)


@handle_errors
def note_tags(note, notebook: NotesBook):
    """
    Retrieves the tags associated with a note in the notebook.

    Args:
        note (str): The name of the note to retrieve the tags for.
        notebook (NotesBook): The notebook to retrieve the tags from.

    Returns:
        list: A list of tags associated with the note.
    """
    tags = notebook.find_note_tags(note)
    if len(tags) > 0:
        rows = [[tag] for tag in tags]
        return table_show(header, rows)
    else:
        return "No tags found for this note"


@handle_errors
def all_tags(notebook: NotesBook):
    """
    Retrieves all tags in the notebook.

    Args:
        notebook (NotesBook): The notebook to retrieve the tags from.

    Returns:
        list: A list of all tags in the notebook.
    """
    tags = notebook.all_tags()
    if len(tags) > 0:
        rows = [[tag] for tag in tags]
        return table_show(header, rows)
    else:
        return "No tags at all"


@handle_errors
def sort_by_tag(order: str, notebook: NotesBook):
    """
    Sorts the notes in the notebook by tag in the specified order.

    Args:
        order (str): The order in which to sort the notes (e.g. "asc" or "desc")
        notebook (NotesBook): The notebook to sort

    Returns:
        str: A string representation of the sorted notebook
    """
    sorted_notes = notebook.sort_by_tag(order)
    if sorted_notes:
        rows = [
            (note.name.value, note.text.value, " ".join(note.tags))
            for note in sorted_notes
        ]
        return table_show(headers, rows)
    else:
        return "No notes found"
