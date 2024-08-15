"""Functions for validation inputs

    Returns:
        bool: returns result of expretions True or False
    """

from datetime import datetime
import re


def input_name_validation(user_input):
    """validation input data for add name

    Args:
        user_input (str): user input in string format

    Returns:
        str: returns user input if passed validation
    """
    if len(user_input) > 0:
        return user_input


def input_number_validation(user_input):
    """validation input data for add number

    Args:
        user_input (str): user input in string format

    Returns:
        str: returns user input if passed validation
    """
    if len(user_input) == 10 and user_input.isdigit():
        return user_input


def input_email_validation(user_input):
    """validation input data for add email

    Args:
        user_input (str): user input in string format

    Returns:
        str: returns user input if passed validation
    """
    pattern = r"\w+@\w+\.\w+"
    match = re.search(pattern, user_input, re.IGNORECASE)
    if match:
        return user_input


def input_address_validation(user_input):
    """validation input data for add address

    Args:
        user_input (str): user input in string format

    Returns:
        str: returns user input if passed validation
    """
    if len(user_input) > 0:
        return user_input


def input_birthday_validation(user_input):
    """validation input data for add bitrhday

    Args:
        user_input (str): user input in string format

    Returns:
        bool: returns result of expretions True or False
    """
    res = True
    try:
        res = bool(datetime.strptime(user_input, "%Y.%m.%d"))
        return res
    except ValueError:
        res = False
        return res

def input_tag_validation(tag: str):
    """
    Validates a tag input by checking if it matches the expected format.

    Args:
        tag (str): The tag to validate.

    Returns:
        bool: True if the tag is valid, False otherwise.
    """
    return re.match(r"#\w+", tag)