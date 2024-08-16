"""Decorators that handle input errors are collected here."""


def input_error(func):
    """Handles a missing arguments error

    Args:
        func (callable): function
    """

    def inner(*args, **kwargs):
        add_contact_message = (
            "Arguments are required. Print 'add username 1234567890', "
            "where username is contact's name, and 1234567890 is contacts phone number: "
            "10 digits only numbers."
        )
        change_contact_message = "Arguments are required. Print 'change username \
1234567890 0987654321', where username is contact's name, and 1234567890 is old \
number and 0987654321 is new number: 10 digits only numbers."
        show_phone_message = "Argument is required. Print 'phone username', \
where username is contact's name."
        delete_contact_message = (
            "Argument is required. Print 'delete all', or 'delete username'."
        )
        add_birthday_message = "YYYY.MM.DD is format for birthday date."
        show_birthday_message = "Arguments are required. Print 'show-birthday username, \
where username is contact's name."
        show_add_phone_message = (
            "The phone number must contain 10 digits, only numbers are required"
        )
        show_edit_contact_input_message = "Arguments are required. Enter edit-contact <name>"
        common_message = "Arguments are required."

        try:
            return func(*args, **kwargs)
        except IndexError:
            if func.__name__ == "show_phone":
                return show_phone_message
            if func.__name__ == "delete_contact":
                return delete_contact_message
            if func.__name__ == "show_birthday":
                return show_birthday_message
            return common_message
        except ValueError:
            if func.__name__ == "add_contact":
                return add_contact_message
            if func.__name__ == "change_contact":
                return change_contact_message
            if func.__name__ == "show_phone":
                return show_phone_message
            if func.__name__ == "delete_contact":
                return delete_contact_message
            if func.__name__ == "add_birthday":
                return add_birthday_message
            if func.__name__ == "show_birthday":
                return show_birthday_message
            if func.__name__ == "add_phone_to_contact":
                return show_add_phone_message
            if func.__name__ == "edit_contact_input":
                print(show_edit_contact_input_message)
            return common_message
        except KeyError as e:
            if func.__name__ == "edit_contact_input":
                print(str(e).strip('"'))
            return f"KeyError: {str(e)}"

    return inner


def empty_contact_list(func):
    """handles an empty contact list error

    Args:
        func (callable): any function that depends on the fullness of the contact list
    """

    def inner(*args, **kwargs):
        if len(args) <= 1:
            if len(args[0]) == 0:
                return "The contacts list is empty. \
Print 'add-contact' to add your first contact."
        elif len(args) > 1:
            if len(args[1]) == 0:
                return "The contacts list is empty. \
Print 'add-contact' to add your first contact."
        return func(*args, **kwargs)

    return inner
