"""functions for save bot name with pickle"""

import pickle
from pathlib import Path
from helpers import custom_print, debug_logger
from .startup_shutdown import pre_welcome


def save_bot_name(bot_name, filename: str = "bot_name.pkl", log_msg=True) -> None:
    """
    Save bot name to a pickle file.

    Args:
        bot_name (str): The bot name to be saved.
        filename (str): The name of the file to save the data to.
        Default is "bot_name.pkl".

    Raises:
        Exception: If an error occurs during the saving process, it will be logged.
    """
    try:
        with Path(filename).open("wb") as f:
            pickle.dump(bot_name, f)
        if log_msg:
            custom_print(
                debug_logger,
                "Bot name successfully saved to {filename}",
                level="info",
                filename=("blue", filename),
            )
    except Exception as e:
        custom_print(
            debug_logger,
            "Error occurred while saving data to {filename} - {e}",
            level="error",
            filename=("blue", filename),
            e=("red", e),
        )


def load_bot_name(filename: str = "bot_name.pkl") -> str:
    """
    Load bot name from a pickle file.

    Args:
        filename (str): The name of the file to load the data from.
        Default is "bot_name.pkl".

    Returns:
        str: The loaded data in string format
        (or string must be a result of the returned func())
        if the file is not found or an error occurs.
    """
    file_path = Path(filename)
    if not file_path.exists():
        custom_print(
            debug_logger,
            "File {filename} not found. Let's create the name to your bot.",
            level="warning",
            filename=("blue", filename),
        )
        return pre_welcome()

    try:
        with file_path.open("rb") as f:
            bot_name = pickle.load(f)
        custom_print(
            debug_logger,
            "Bot name successfully loaded from {filename}",
            level="info",
            filename=("blue", filename),
        )
        return bot_name
    except (pickle.UnpicklingError, EOFError) as e:
        custom_print(
            debug_logger,
            "Error occurred while loading data from {filename} - {e}",
            level="error",
            filename=("blue", filename),
            e=("red", e),
        )
        return pre_welcome()
    except Exception as e:
        custom_print(
            debug_logger,
            "Unknown error occurred while loading data from {filename} - {e}",
            level="critical",
            filename=("blue", filename),
            e=("red", e),
        )
        return pre_welcome()
