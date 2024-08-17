"""Module with creating and adding the name of the main bot"""


def create_bot_name():
    """Creates the name of the main bot

    Returns:
        str: bot name in string format
    """
    bot_name = input(">>> ").upper()
    return bot_name


def edit_bot_name(current_bot_name):
    """Changes the name of the main bot

    Returns:
        str: new bot name in string format
    """

    print(f"Bot name now is {current_bot_name}")
    while True:
        y_or_n = input("Do you want to change it? y/n ").lower().strip()
        if y_or_n in ["y", "n"]:
            if y_or_n == "y":
                new_bot_name = input("Enter new name for your bot: ").upper()
                if new_bot_name:
                    break
            break
    return new_bot_name
