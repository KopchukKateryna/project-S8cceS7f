"""An addition input module for adding the first contact,
his phone number, email, address, birthday
    """

from handlers import (
    add_contact,
    add_phone_to_contact,
    add_email_to_contact,
    add_address_to_contact,
    add_birthday,
)


def input_contact_name():
    contact_name = input("Enter contact's name: ").lower()
    if len(contact_name) == 0:
        print("The name must contain at least one symbol")
        input_contact_name()
    return contact_name


def input_contact_phone():
    contact_phone = input("Enter contact's phone number: ").lower()
    # валідація номеру
    if len(contact_phone) == 10 and contact_phone.isdigit():
        return contact_phone
    else:
        print("The phone number must contain 10 only numbers")
        input_contact_phone()


def input_contact_email():
    contact_email = input("Enter contact's email: ").lower()
    if len(contact_email) == 0:
        print("The email must contain at least 5 symbols")
        input_contact_email()
    # тут має бути валідація имейл
    return contact_email


def input_contact_birthday():
    contact_birthday = input("Enter contact's birthday: ").lower()
    if len(contact_birthday) == 0:
        input_contact_birthday()
    # тут потрібна валідація дня народження
    # без адекватної валідації буде невірно працювати при невалідному форматі дати
    return contact_birthday


def input_contact_address():
    contact_address = input("Enter contact's address: ").lower()
    if len(contact_address) == 0:
        input_contact_address()
    return contact_address


def add_contact_input(book):
    """An addition input module for adding the first contact,
    his phone number, email, address, birthday

        Args:
            book (class): contact list
    """

    contact_name = input_contact_name()
    print(add_contact(contact_name, book))

    contact_phone = input_contact_phone()
    args = [contact_name, contact_phone]
    print(add_phone_to_contact(args, book))

    def email_input_y_or_n():
        email_input = input("Do you want to add email y/n: ").lower()
        if email_input != "y" and email_input != "n":
            email_input_y_or_n()
        if email_input == "y":
            contact_email = input_contact_email()
            args = [contact_name, contact_email]
            print(add_email_to_contact(args, book))
        if email_input == "n":
            pass

    email_input_y_or_n()

    def birthday_input_y_or_n():
        birthday_input = input("Do you want to add birthday y/n: ").lower()
        if birthday_input != "y" and birthday_input != "n":
            birthday_input_y_or_n()
        if birthday_input == "y":
            contact_birthday = input_contact_birthday()
            args = [contact_name, contact_birthday]
            print(add_birthday(args, book))

        if birthday_input == "n":
            pass

    birthday_input_y_or_n()

    def address_input_y_or_n():
        address_input = input("Do you want to add address y/n: ").lower()
        if address_input != "y" and address_input != "n":
            address_input_y_or_n()
        if address_input == "y":
            contact_address = input_contact_address()
            args = [contact_name, contact_address]
            print(add_address_to_contact(args, book))
        if address_input == "n":
            pass

    address_input_y_or_n()
