from ..validations import (
    input_name_validation,
    input_number_validation,
    input_email_validation,
    input_address_validation,
    input_birthday_validation,
)

from .fields_handlers import (
    edit_name,
    add_phone,
    edit_phone,
    delete_phone,
    add_email,
    edit_email,
    delete_email,
    add_address,
    edit_address,
    delete_address,
    add_birthday,
    edit_birthday,
    delete_birthday,
)


def edit_phone_in_contacts(old_phone, record):
    while True:
        new_phone = input("Enter new phone: ").lower().strip()
        if input_number_validation(new_phone):
            print(edit_phone(old_phone, new_phone, record))
            break
        print("The phone number must contain 10 only numbers")


def edit_email_in_contacts(record):
    while True:
        new_email = input("Enter new email: ").lower().strip()
        if input_email_validation(new_email):
            print(edit_email(new_email, record))
            break
        print("The phone number must contain 10 only numbers")


def edit_address_in_contacts(record):
    while True:
        new_address = input("Enter new address: ").lower()
        if input_address_validation(new_address):
            print(edit_address(new_address, record))
            break
        print("Address must contain at least one symbol")


def edit_birthday_in_contacts(record):
    while True:
        new_birthday = input("Enter new birthday: ").lower()
        if input_birthday_validation(new_birthday):
            print(edit_birthday(new_birthday, record))
            break
        print("Invalid date format. Use YYYY.MM.DD")


def edit_name_action(old_name, record, book):
    while True:
        new_name = input("Enter new name: ").lower()
        if input_name_validation(new_name):
            print(edit_name(old_name, new_name, record, book))
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
