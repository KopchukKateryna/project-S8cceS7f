from handlers import (
    add_birthday,
    add_contact,
    change_contact,
    delete_contact,
    parse_input,
    show_all,
    show_birthday,
    show_phone,
    show_upcoming_birthdays,
    search_contact,
)
from helpers import setup_logging
from helpers.assistant_info import assistant_info
from helpers.pickle_utils import load_data, save_data

logger = setup_logging()


def main():
    """The main function of the bot, manages the main cycle of command processing"""
    book = load_data()
    print("Welcome to the assistant bot!")
    print(
        (
            "The table below summarizes information about the commands. "
            "But if you forget something in the process, just call the 'info' command "
            "and you will see this table again."
        )
    )
    print(assistant_info())
    print()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        if command == "hello":
            print("How can I help you?")

        elif command == "info":
            print(assistant_info())

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "delete":
            print(delete_contact(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(show_upcoming_birthdays(book))

        elif command == "search":
            print(search_contact(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
