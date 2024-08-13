"""Record class"""

from classes.birthday import Birthday
from classes.name import Name
from classes.phone import Phone


class Record:
    """
    A class for storing contact information, including name and phone numbers.

    Attributes:
        * name (Name) - The contact's name.
        * phones (list of Phone) - A list of the contact's phone numbers.
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        contact_string = (
            f"Contact name: {self.name.value}, phones: "
            f"{'; '.join(p.value for p in self.phones)}"
        )

        if self.birthday:
            contact_string += f", birthday: {self.birthday}"

        return contact_string

    def add_phone(self, number: str):
        """
        Add a phone number to the record.

        Args:
            * phone (str) - The phone number to be added.
        """
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        """
        Remove a phone number from the record.

        Args:
            * phone (str) - The phone number to be removed.
        """

        self.phones = list(filter(lambda phone: phone == number, self.phones))

    def edit_phone(self, old_number: str, new_number: str):
        """
        Edit a phone number in the record.

        Args:
            * old_phone (str) - The phone number to be replaced.
            * new_phone (str) - The new phone number to replace the old one.
        """

        self.phones = list(
            map(
                lambda phone: Phone(new_number) if phone.value == old_number else phone,
                self.phones,
            )
        )

    def find_phone(self, number):
        """
        Find a phone number in the record.

        Args:
            * phone (str) - The phone number to find.

        Returns:
            * Phone - The phone object if found, None otherwise.
        """

        for phone in self.phones:
            if phone.value == number:
                return phone

    def add_birthday(self, date_of_birthday):
        """Add a birthday to the record."""
        self.birthday = Birthday(date_of_birthday)
