from handlers import (
    add_birthday,
    add_contact,
    add_note,
    change_contact,
    delete_contact,
    parse_input,
    show_all,
    show_birthday,
    show_phone,
    show_upcoming_birthdays,
    show_all_notes,
    search_contact,
    add_email_to_contact,
    add_phone_to_contact,
    add_address_to_contact,
    add_contact_input
)
from helpers import setup_logging
from helpers.assistant_info import assistant_info
from helpers.pickle_utils import load_data, save_data
from classes import NotesBook

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

    notes_book = NotesBook()

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

        # elif command == "add":
        #     print(add_contact(args, book))

        elif command == "add":
            print(add_contact(args, book))

        elif command == "add-note":
            print(add_note(notes_book))
        elif command == "add-contact":
            contact_name = input("Enter contact's name: ").lower()
            print(add_contact(contact_name, book))
            contact_phone = input("Enter contact's phone number: ").lower()
            print(add_phone_to_contact(contact_name, contact_phone, book))

            email_input = input("Do you want to add email y/n: ").lower()
            if email_input == "y":
                contact_email = input("Enter contact's email: ").lower()
                args = [contact_name, contact_email]
                print(add_email_to_contact(args, book))
            if email_input == "n":
                pass

            birthday_input = input("Do you want to add birthday y/n: ").lower()
            if birthday_input == "y":
                contact_birthday = input("Enter contact's birthday: ").lower()
                args = [contact_name, contact_birthday]
                print(add_birthday(args, book))
            if email_input == "n":
                pass

            address_input = input("Do you want to add address y/n: ").lower()
            if address_input == "y":
                contact_address = input("Enter contact's address: ").lower()
                args = [contact_name, contact_address]
                print(add_address_to_contact(args, book))
            if email_input == "n":
                pass
            add_contact_input(book)

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "all-notes":
            print(show_all_notes(notes_book))

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
        elif command == "add-phone":
            print(add_phone_to_contact(args, book))

        elif command == "add-email":
            print(add_email_to_contact(args, book))

        elif command == "add-address":
            print(add_address_to_contact(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
