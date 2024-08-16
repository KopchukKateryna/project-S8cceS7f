"""An addition input module for adding the first contact,
    his phone number, email, address, birthday
    """

from handlers import (
    add_contact,
    add_phone_to_contact,
    add_email_to_contact,
    add_address_to_contact,
    add_birthday_to_contact,
)

from ..validations import (
    input_name_validation,
    input_number_validation,
    input_email_validation,
    input_address_validation,
    input_birthday_validation,
)


def add_contact_input(book):
    """An addition input module for adding the first contact,
    his phone number, email, address, birthday

        Args:
            book (class): class AddressBook that contains all contacts
    """

    while True:
        user_input = input("Enter contact's name: ").lower()
        if input_name_validation(user_input):
            contact_name = user_input
            print(add_contact(contact_name, book))
            break
        print("The name must contain at least one symbol")

    while True:
        user_input = input("Enter contact's phone number: ").lower()
        if input_number_validation(user_input):
            contact_phone = user_input
            args = [contact_name, contact_phone]
            print(add_phone_to_contact(args, book))
            break
        print("The phone number must contain 10 only numbers")

    while True:
        y_n_input = input("Do you want to add email y/n: ").lower()
        if y_n_input == "y" or y_n_input == "n":
            if y_n_input == "y":
                while True:
                    user_input = input("Enter contact's email: ").lower()
                    if input_email_validation(user_input):
                        contact_email = user_input
                        args = [contact_name, contact_email]
                        print(add_email_to_contact(args, book))
                        break
                    print("Email format: email@email.com")
                break
            break

    while True:
        y_n_input = input("Do you want to add address y/n: ").lower()
        if y_n_input == "y" or y_n_input == "n":
            if y_n_input == "y":
                while True:
                    user_input = input("Enter contact's address: ").lower()
                    if input_address_validation(user_input):
                        contact_address = user_input
                        args = [contact_name, contact_address]
                        print(add_address_to_contact(args, book))
                        break
                    print("Address must contain at least one symbol")
                break
            break

    while True:
        y_n_input = input("Do you want to add birthday y/n: ").lower()
        if y_n_input == "y" or y_n_input == "n":
            if y_n_input == "y":
                while True:
                    user_input = input("Enter contact's birthday: ").lower()
                    if input_birthday_validation(user_input):
                        contact_birthday = user_input
                        args = [contact_name, contact_birthday]
                        print(add_birthday_to_contact(args, book))
                        break
                    print("Invalid date format. Use YYYY.MM.DD")
                break
            break
