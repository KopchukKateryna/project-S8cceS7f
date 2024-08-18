"""functions for work with pickle"""

import pickle
from pathlib import Path
from helpers import custom_print, debug_logger
from classes import NotesBook


def save_notes(notebook: NotesBook, filename: str = "notesbook.pkl") -> None:
    """
    Save data to a pickle file.

    Args:
        notebook (NotesBook): The object to be saved (e.g., an instance of NotesBook).
        filename (str): The name of the file to save the data to.
        Default is "NotesBook.pkl".

    Raises:
        Exception: If an error occurs during the saving process, it will be logged.
    """
    try:
        with Path(filename).open("wb") as f:
            pickle.dump(notebook, f)
            custom_print(
                debug_logger,
                "Data successfully saved to {filename}",
                level="info",
                filename=("blue", filename),
            )
    except Exception as e:
        custom_print(
            debug_logger,
            "Error occurred while saving data from {filename} - {e}",
            level="error",
            filename=("blue", filename),
            e=("red", e),
        )


def load_notes(filename: str = "notesbook.pkl") -> NotesBook:
    """
    Load data from a pickle file.

    Args:
        filename (str): The name of the file to load the data from.
        Default is "NotesBook.pkl".

    Returns:
        Any: The loaded data, or a new instance of NotesBook
        if the file is not found or an error occurs.
    """
    file_path = Path(filename)
    if not file_path.exists():
        custom_print(
            debug_logger,
            "File {filename} not found. Returning a new NotesBook instance.",
            level="warning",
            filename=("blue", filename),
        )
        return NotesBook()

    try:
        with file_path.open("rb") as f:
            data = pickle.load(f)
        custom_print(
            debug_logger,
            "Data successfully loaded from {filename}",
            level="info",
            filename=("blue", filename),
        )
        return data
    except (pickle.UnpicklingError, EOFError) as e:
        custom_print(
            debug_logger,
            "Error occurred while loading data from {filename} - {e}",
            level="error",
            filename=("blue", filename),
            e=("red", e),
        )
        return NotesBook()
    except Exception as e:
        custom_print(
            debug_logger,
            "Unknown error occurred while loading data from {filename} - {e}",
            level="critical",
            filename=("blue", filename),
            e=("red", e),
        )
        return NotesBook()
