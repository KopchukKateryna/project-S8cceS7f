"""Contact Table Formatter class"""


class ContactTableFormatter:
    """Contact Table Formatter class"""

    @staticmethod
    def format_contacts(records_by_email_generator):
        """
        Formats a list of contacts from a records generator into an array.

        This method accepts a generator of contact records, extracts the necessary
        data (name, phone, birthday, email, address), and returns them in the form
        of an array where each element is a nested array containing two strings:
        the contact's name and a string with the rest of the information.

        Fields that are missing or have a value of `None`
        are excluded from the final string.
        Args:
            records_by_email_generator (generator): A generator of contact objects,
            each containing fields such as `name`, `phone`, `birthday`,
            `email`, and `address`.

        Returns:
            list: A list where each element is a nested list containing two strings.
            The first string is the contact's name, and the second is a string with
            the rest of the information.
        """
        return [
            [
                record.name,
                ", ".join(
                    filter(
                        None,
                        [
                            (
                                f"phones: "
                                f"{', '.join([str(phone) for phone in record.phones])}"
                                if record.phones
                                else None
                            ),
                            f"birthday: {record.birthday}" if record.birthday else None,
                            (
                                f"email: {record.email}"
                                if hasattr(record, "email") and record.email
                                else None
                            ),
                            f"address: {record.address}" if record.address else None,
                        ],
                    )
                ),
            ]
            for record in records_by_email_generator
        ]
