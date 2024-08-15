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
from .decorators import input_error, empty_contact_list


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


"""
    Contacts handlers
    \/\/\/\/\/\/\/\/
                    """

def edit_name(name, record):
    record.edit_name(name)
    return "Name updated"

"""Phone handlers"""

def add_phone(number, record):
    record.add_phone(number)
    return "Phone added."

def delete_phone(number, record):
    if len(record.phones) == 1:
        return "This is the only phone number. You cannot delete it"
    record.remove_phone(number)
    return "Phone deleted."

def edit_phone(old_phone, new_phone, record):
    record.edit_phone(old_phone, new_phone)
    return "Phone changed."

def edit_phone_in_contacts(old_phone, record):
    while True:
        new_phone = input("Enter new phone: ").lower().strip()
        if input_number_validation(new_phone):
            print(edit_phone(old_phone, new_phone, record))
            break
        print("The phone number must contain 10 only numbers")

"""Email handlers"""

def add_email(email, record):
    record.add_email(email)
    return "Email added."

def edit_email(email, record):
    record.edit_email(email)
    return "Email updated."

def delete_email(record):
    record.remove_email()
    return "Email deleted."

def edit_email_in_contacts(record):
    while True:
        new_email = input("Enter new email: ").lower().strip()
        if input_email_validation(new_email):
            print(edit_email(new_email, record))
            break
        print("The phone number must contain 10 only numbers")

"""Address handlers"""

def add_address(address, record):
    record.add_address(address)
    return "Address added."

def edit_address(address, record):
    record.edit_address(address)
    return "Address updated."

def delete_address(record):
    record.remove_address()
    return "Address deleted."

def edit_address_in_contacts(record):
    while True:
        new_address = input("Enter new address: ").lower()
        if input_address_validation(new_address):
            print(edit_address(new_address, record))
            break
        print("Address must contain at least one symbol")

def add_birthday(birthday, record):
    record.add_birthday(birthday)
    return "Birthday added."

def edit_birthday(birthday, record):
    record.edit_birthday(birthday)
    return "Birthday updated."

def delete_birthday(record):
    record.remove_birthday()
    return "Birthday deleted."

def edit_birthday_in_contacts(record):
    while True:
        new_birthday = input("Enter new birthday: ").lower()
        if input_birthday_validation(new_birthday):
            print(edit_birthday(new_birthday, record))
            break
        print("Invalid date format. Use YYYY.MM.DD")

"""
    Choises
    \/\/\/\/
            """

def edit_or_delete_phone_choise(number, record):
    while True:
        edit_or_delete_input = input("Do you want to edit or delete it? ")
        if edit_or_delete_input in ["edit", "delete"]:
            if edit_or_delete_input == "edit":
                edit_phone_in_contacts(number, record)
                break
            if edit_or_delete_input == "delete":
                print(delete_phone(number, record))
                break

def add_or_not_phone_choise(old_phone, record):
    while True:
        y_or_n = input("Do you want to add it? y/n ").lower().strip()
        if y_or_n == "y" or y_or_n == "n":
            if y_or_n == "y":
                print(add_phone(old_phone, record))
                break
            break


def edit_or_delete_email_choise(record):
    while True:
        edit_or_delete_input = input("Do you want to edit or delete it? ")
        if edit_or_delete_input in ["edit", "delete"]:
            if edit_or_delete_input == "edit":
                edit_email_in_contacts(record)
                break
            print(delete_email(record))
            break

def add_or_not_email_choise(record):
    while True:
        y_or_n = input("Do you want to add it? y/n ").lower().strip()
        if y_or_n == "y" or y_or_n == "n":
            if y_or_n == "y":
                add_email_action(record)
                break
            break


def edit_or_delete_address_choise(record):
    while True:
        edit_or_delete_input = input("Do you want to edit or delete it? ")
        if edit_or_delete_input in ["edit", "delete"]:
            if edit_or_delete_input == "edit":
                edit_address_in_contacts(record)
                break
            print(delete_address(record))
            break

def add_or_not_address_choise(record):
    while True:
        y_or_n = input("Do you want to add it? y/n ").lower().strip()
        if y_or_n == "y" or y_or_n == "n":
            if y_or_n == "y":
                add_address_action(record)
                break
            break


def edit_or_delete_birthday_choise(record):
    while True:
        edit_or_delete_input = input("Do you want to edit or delete it? ")
        if edit_or_delete_input in ["edit", "delete"]:
            if edit_or_delete_input == "edit":
                edit_birthday_in_contacts(record)
                break
            print(delete_birthday(record))
            break

def add_or_not_birthday_choise(record):
    while True:
        y_or_n = input("Do you want to add it? y/n ").lower().strip()
        if y_or_n == "y" or y_or_n == "n":
            if y_or_n == "y":
                add_birthday_action(record)
                break
            break

"""
    Actions
    \/\/\/\/
            """

def edit_name_action(record, book):
    while True:
        new_name = input("Enter new name: ").lower()
        if input_name_validation(new_name):
            print(edit_name(new_name, record))
            break
        print("The name must contain at least one symbol")

def add_phone_action(record):
    while True:
        number = input("Enter phone number to add: ").lower().strip()
        if input_number_validation(number):
            number_in_contacts = record.find_phone(number)
            if number_in_contacts:
                print(f"Number {number} already exist.")
                edit_or_delete_phone_choise(number, record)
                break
            print(add_phone(number, record))
            break
        print("The phone number must contain 10 only numbers")

def edit_phone_action(record):
    while True:
        old_phone = input("Enter phone number to edit: ").lower().strip()
        if input_number_validation(old_phone):
            number_in_contacts = record.find_phone(old_phone)
            if not number_in_contacts:
                print(f"Number {old_phone} has not found.")
                add_or_not_phone_choise(old_phone, record)
                break
            edit_or_delete_phone_choise(old_phone, record)
            break
        print("The phone number must contain 10 only numbers")

def delete_phone_action(record):
    while True:
        number = input("Enter phone number to delete: ").lower().strip()
        if input_number_validation(number):
            number_in_contacts = record.find_phone(number)
            if not number_in_contacts:
                print(f"Number {number} has not found.")
                break
            print(delete_phone(number, record))
            break
        print("The phone number must contain 10 only numbers")
        
def add_email_action(record):
    while True:
        email = input("Enter email to add: ").lower().strip()
        if input_email_validation(email):
            print(add_email(email, record))
            break
        print("Email format: email@email.com")

def add_address_action(record):
    while True:
        address = input("Enter address to add: ").lower()
        if input_address_validation(address):
            print(add_address(address, record))
            break
        print("Address must contain at least one symbol")

def add_birthday_action(record):
    while True:
        birthday = input("Enter birthday to add: ").lower().strip()
        if input_birthday_validation(birthday):
            print(add_birthday(birthday, record))
            break
        print("Invalid date format. Use YYYY.MM.DD")

@input_error
def edit_contact_input(args, book):
    record = None
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError(f"No such name '{name}' was found")
    
    while True:
        field_to_edit = input("What field do you want to edit? ").lower()
        if field_to_edit in ["name", "phones", "email", "address", "birthday"]:

            # Змінити імʼя, видалити імʼя не можна
            if field_to_edit == "name":
                edit_name_action(record, book)


            if field_to_edit == "phones":
                while True:
                    print("You can add, edit, delete phone, or exit")
                    action = input("What do you want to do?  ")
                    if action in ["add", "edit", "delete"]:
                        if action == "add":
                            add_phone_action(record)
                        if action == "edit":
                            edit_phone_action(record)
                        if action == "delete":
                            delete_phone_action(record)
                    if action == "exit":
                        break

            if field_to_edit == "email":
                while True:
                    if record.email:
                        edit_or_delete_email_choise(record)
                        break
                    print(f"Contact {name} has no email yet.")
                    add_or_not_email_choise(record)
                    break

            if field_to_edit == "address":
                while True:
                    if record.address:
                        edit_or_delete_address_choise(record)
                        break
                    print(f"Contact {name} has no address yet.")
                    add_or_not_address_choise(record)
                    break

            if field_to_edit == "birthday":
                while True:
                    if record.birthday:
                        edit_or_delete_birthday_choise(record)
                        break
                    print(f"Contact {name} has no birthday yet.")
                    add_or_not_birthday_choise(record)
                    break

        if field_to_edit == "exit":
            break
