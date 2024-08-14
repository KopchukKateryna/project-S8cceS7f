"""class NotesBook"""

from collections import UserDict
from classes.note import Note
import re


class NotesBook(UserDict):
    """
    A class to manage a collection of notes.

    Inherits from UserDict to store and manage Note instances.

    Attributes:
        data (dict): A dictionary to store notes using their name as the key.
    """

    def __init__(self):
        """
        Initializes a NotesBook instance.
        """
        super().__init__()

    def __str__(self):
        """
        Returns a string representation of all notes in the NotesBook.

        Returns:
            str: A formatted string with each note's details.
        """
        lines = [str(note) for note in self.data.values()]
        return "\n".join(lines)

    def add_note(self, note):
        """
        Adds a note to the NotesBook.

        Args:
            note (Note): The note to add.

        Raises:
            KeyError: If a note with the same name already exists.
        """
        if note.name.value in self.data:
            raise KeyError(f"Note with name '{note.name.value}' already exists.")
        self.data[note.name.value] = note

    def find(self, name) -> Note:
        """
        Finds a note by its name.

        Args:
            name (str): The name of the note to find.

        Returns:
            Note or None: The note if found, or None if not found.
        """
        return self.data.get(name, None)
    
    def add_tag(self, note_name, tag) -> str:
        note = self.find(note_name)
     
        if note:
               if not self.__validate_tag(tag):
                    return note.add_tag(tag)
               else: 
                    return "Not valid tag name"
        else:
            return f"Note with this name: {note_name} not found"
        
    def add_tags(self, note_name, tags: str) -> str:
        note = self.find(note_name)
        if note:
             tags = self.__split_tags(tags)
             if len(tags) > 0:
                 for tag in tags:
                    note.add_tag(tag)
                 return "Tags added succesfully"
             else:
                 return "Input tags please"
        else:
             return f"Note with this name: {note_name} not found"

    def edit_tag(self, note_name, old_tag, new_tag) -> str:
        note = self.find(note_name)
     
        if note:
               if not self.__validate_tag(old_tag):
                    return note.edit_tag(old_tag, new_tag)
               else: 
                    return "Not valid tag name"
        else:
            return f"Note with this name: {note_name} not found"        

        
    def remove_tag(self, note_name, tag) -> str:
        note = self.find(note_name)
        if note:
            if not self.__validate_tag(tag):
                return note.remove_tag(tag)
            else: 
                return "Not valid tag name"
        else:
            return f"Note with this name: {note_name} not found"
        
    def remove_tags(self, note_name, tags: str) -> str:
        note = self.find(note_name)
        if note:
             tags = self.__split_tags(tags)
             if len(tags) > 0:
                 for tag in tags:
                    note.remove_tag(tag)
                 return "Tags removed succesfully"
             else:
                 return "Input tags please"
        else:
             return f"Note with this name: {note_name} not found"     
    
    def find_tag(self, note_name, tag) -> str:
        note = self.find(note_name)
        if note:
            return note.find_tag(tag)
        else:
            return f"Note with this name: {note_name} not found"
        
    def all_tags_by_note_name(self, note_name) -> str:
        note = self.find(note_name)
        if note:
            return note.tags
        else:
            return f"Note with this name: {note_name} not found"
        
    def all_tags(self) -> set:
        tags = set()
        if len(self.data) > 0:
            for note in self.data.values:
                tags.update(note.tags)
        return tags

    
    def __split_tags(self, tags: str) -> list:
        return re.split(r"\B#\w+", tags)
    
    def __validate_tag(self, tag: str) -> bool:
        return re.match(r"\B#\w+", tag)
