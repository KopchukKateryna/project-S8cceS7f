"""functions for save bot name with pickle"""

import logging
import pickle
from pathlib import Path
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
            logging.info("Bot name successfully saved to %s", filename)
    except Exception as e:
        logging.error("Error occurred while saving data to %s: %s", filename, e)


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
        logging.warning(
            "File %s not found. Let's create the name to your bot.", filename
        )
        return pre_welcome()

    try:
        with file_path.open("rb") as f:
            bot_name = pickle.load(f)
        logging.info("Bot name successfully loaded from %s", filename)
        return bot_name
    except (pickle.UnpicklingError, EOFError) as e:
        logging.error("Error occurred while loading data from %s: %s", filename, e)
        return pre_welcome()
    except Exception as e:
        logging.critical(
            "Unknown error occurred while loading data from %s: %s", filename, e
        )
        return pre_welcome()
