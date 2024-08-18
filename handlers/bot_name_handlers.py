"""Module with creating and adding the name of the main bot"""

from helpers import custom_print, command_logger


def create_bot_name():
    """Creates the name of the main bot

    Returns:
        str: bot name in string format
    """
    bot_name = input(">> ").upper()
    return bot_name


def edit_bot_name(current_bot_name):
    """Changes the name of the main bot

    Returns:
        str: new bot name in string format
    """

    print(f"Bot name now is {current_bot_name}")
    while True:
        custom_print(
            command_logger,
            "Do you want to change it? {y}/{n}: ",
            space="top",
            level="info",
            y=("bright_magenta"),
            n=("bright_magenta"),
        )
        y_or_n = input(">> ").lower().strip()
        if y_or_n in ["y", "n"]:
            if y_or_n == "y":
                custom_print(
                    command_logger,
                    "{msg}",
                    space="top",
                    level="info",
                    msg=("cyan", "Please, enter new name for your bot: "),
                )
                new_bot_name = input(">> ").upper()
                if new_bot_name:
                    break
            break
    return new_bot_name
