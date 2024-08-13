
from handlers import (
    add_contact, 
    add_phone_to_contact, 
    add_email_to_contact, 
    add_address_to_contact, 
    add_birthday
    )

def add_contact_input(book):
    contact_name = input("Enter contact's name: ").lower()
    print(add_contact(contact_name, book))
    contact_phone = input("Enter contact's phone number: ").lower()
    args = [contact_name, contact_phone]
    print(add_phone_to_contact(args, book))

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