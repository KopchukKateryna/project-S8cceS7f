"""Decorators that handle input errors are collected here."""

from helpers import custom_print, command_logger


def print_msg(msg: str):
    """Prints a message to the console."""
    custom_print(
        command_logger,
        msg,
        space="top",
        level="warning",
    )


def input_error(func):
    """Handles a missing arguments error

    Args:
        func (callable): function
    """

    def inner(*args, **kwargs):
        # parse_input_message = ("Invalid command")
        add_contact_message = (
            "Arguments are required. Print 'add name 1234567890', "
            "where name is contact's name, and 1234567890 is contacts phone number: "
            "10 digits numbers only."
        )
        change_contact_message = "Arguments are required. Print 'change name \
number new-number', where name is contact's name, and number is old \
number and then a new number: 10 digits numbers only."
        show_phone_message = "Argument is required. Print 'phone name', \
where name is contact's name."
        delete_contact_message = (
            "Argument is required. Print 'delete all', or 'delete name'."
        )
        add_birthday_message = "DD.MM.YYYY is format for birthday date."
        show_birthday_message = "Arguments are required. Print 'show-birthday name', \
where name is contact's name."
        show_add_phone_message = (
            "The phone number must contain 10 digits, only numbers are required"
        )
        show_edit_contact_input_message = (
            "Arguments are required. Enter edit-contact <name>"
        )
        search_contact_message = "Arguments are required. \
Enter search-contact <name> | <email> | <phone> | <address> | <birthday>"
        common_message = "Arguments are required."

        try:
            return func(*args, **kwargs)
        except IndexError as i:
            if func.__name__ == "show_phone":
                print_msg(show_phone_message)
                return show_phone_message
            if func.__name__ == "delete_contact":
                print_msg(delete_contact_message)
                return delete_contact_message
            if func.__name__ == "show_birthday":
                print_msg(show_birthday_message)
                return show_birthday_message
            if func.__name__ == "show_upcoming_birthdays":
                print_msg(str(i).strip("'"))
                return str(i).strip("'")
            return common_message
        except ValueError:
            if func.__name__ == "add_contact":
                print_msg(add_contact_message)
                return add_contact_message
            if func.__name__ == "change_contact":
                print_msg(change_contact_message)
                return change_contact_message
            if func.__name__ == "show_phone":
                print_msg(show_phone_message)
                return show_phone_message
            if func.__name__ == "delete_contact":
                print_msg(delete_contact_message)
                return delete_contact_message
            if func.__name__ == "add_birthday":
                print_msg(add_birthday_message)
                return add_birthday_message
            if func.__name__ == "show_birthday":
                print_msg(show_birthday_message)
                return show_birthday_message
            if func.__name__ == "add_phone_to_contact":
                print_msg(show_add_phone_message)
                return show_add_phone_message
            if func.__name__ == "edit_contact_input":
                print_msg(show_edit_contact_input_message)
            if func.__name__ == "search_contact":
                print_msg(search_contact_message)
                return search_contact_message
            return common_message
        except KeyError as e:
            if func.__name__ == "edit_contact_input":
                print_msg(str(e).strip('"'))

            return str(e).strip("'")

    return inner


def empty_contact_list(func):
    """handles an empty contact list error

    Args:
        func (callable): any function that depends on the fullness of the contact list
    """

    def inner(*args, **kwargs):
        if len(args) <= 1:
            if len(args[0]) == 0:
                custom_print(
                    command_logger,
                    "The contacts list is empty. \
Type 'add-contact' to add your first contact.",
                    space="top",
                    level="warning",
                )
                return
        elif len(args) > 1:
            if len(args[1]) == 0:
                custom_print(
                    command_logger,
                    "The contacts list is empty. \
Type 'add-contact' to add your first contact.",
                    space="top",
                    level="warning",
                )
                return
        return func(*args, **kwargs)

    return inner
