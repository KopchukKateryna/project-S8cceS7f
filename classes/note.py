"""class Note"""

from classes.field import Field

class Note:
    """
    A class representing a note with a name and text.

    Attributes:
        name (Field): The name of the note.
        text (Field): The text content of the note.
    """

    def __init__(self, name, text=""):
        """
        Initializes a Note instance with a name and optional text.

        Args:
            name (str): The name of the note.
            text (str, optional): The text content of the note. Defaults to empty string.
        """
        self.text = Field(text)
        self.name = Field(name)
        self.__tags = set()

    def __str__(self):
        """
        Returns a string representation of the note.

        Returns:
            str: A formatted string with the note's name and text.
        """
        return f"Note: {self.name.value}, Text: {self.text.value}, Tag: {self.tags}"
    
    @property
    def tags(self) -> set:
        return self.__tags
    
    def add_tag(self, tag: str) -> str:
        if not self.has_tag(tag):
            self.__tags.add(tag)
            return f"{tag} added successfully"
        else:
            return f"{tag} already is used for note"

        
    def remove_tag(self, tag: str):
        if self.has_tag(tag):
            self.__tags.remove(tag)
            return f"{tag} removed successfully"
        else:
            return f"{tag} not use for this note"
        
    def edit_tag(self, old_tag: str, new_tag: str):
        if self.has_tag(old_tag):
            self.__tags.remove(old_tag)
            self.__tags.add(new_tag)
            return f"{old_tag} changed successfully"
        else:
            return f"{old_tag} not use for this note"
        
    def find_tag(self, tag: str) -> str:
        if self.has_tag(tag):
            return self.__str__()
        
    def has_tag(self, tag: str) -> bool:
        return tag in self.__tags      
