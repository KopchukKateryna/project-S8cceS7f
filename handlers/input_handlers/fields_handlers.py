"""Here are all the handlers to work with contact fields
    """

def edit_name(old_name, new_name, record, book):
    """Edit the name field"""
    record.edit_name(new_name)
    book.add_record(record)
    book.delete(old_name)
    
    return "Name updated"

"""Phone handlers"""

def add_phone(number, record):
    """Edd the phone"""
    record.add_phone(number)
    return "Phone added."

def delete_phone(number, record):
    """Delete phone"""
    if len(record.phones) == 1:
        return "This is the only phone number. You cannot delete it"
    record.remove_phone(number)
    return "Phone deleted."

def edit_phone(old_phone, new_phone, record):
    """Edit phone"""
    record.edit_phone(old_phone, new_phone)
    return "Phone changed."

"""Email handlers"""

def add_email(email, record):
    """Add email"""
    record.add_email(email)
    return "Email added."

def edit_email(email, record):
    """Edit email"""
    record.edit_email(email)
    return "Email updated."

def delete_email(record):
    """Delete email"""
    record.remove_email()
    return "Email deleted."

"""Address handlers"""

def add_address(address, record):
    """Add address"""
    record.add_address(address)
    return "Address added."

def edit_address(address, record):
    """Edit adress"""
    record.edit_address(address)
    return "Address updated."

def delete_address(record):
    """Delete address"""
    record.remove_address()
    return "Address deleted."

"""Birthday handlers"""

def add_birthday(birthday, record):
    """Add birthday"""
    record.add_birthday(birthday)
    return "Birthday added."

def edit_birthday(birthday, record):
    """Edit birthday"""
    record.edit_birthday(birthday)
    return "Birthday updated."

def delete_birthday(record):
    """Delete birthday"""
    record.remove_birthday()
    return "Birthday deleted."
