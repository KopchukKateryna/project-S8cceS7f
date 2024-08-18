"""
Module for creating custom command autocompletions in
a console application using prompt_toolkit.

This module provides an autocomplete functionality that allows users
to choose from a list of full commands, including their abbreviated versions.
When a command is selected from the autocomplete list, only the full command
is inserted into the input line.
"""

from prompt_toolkit.completion import Completer, Completion


class CustomWordCompleter(Completer):
    """
    A class to create command autocompletions with support for
    abbreviated command versions.

    This class is intended for use in a console application,
    leveraging prompt_toolkit for autocompletions.
    It provides the functionality to autocomplete commands where each
    command may have ONE or MORE abbreviated versions.
    In the dropdown list of autocompletions, the command is displayed with its
    abbreviation, but only the full command is inserted when selected.

    Attributes:
    -----------
    commands : list of str
        The list of full commands available for autocompletion.
    corrections : dict
        A dictionary where the keys are abbreviated versions of the commands,
        and the values are the full commands.
    ignore_case : bool, optional
        A flag indicating whether to ignore case sensitivity when
        matching (default is True).

    Methods:
    --------
    get_completions(document, complete_event):
        Generates a list of possible completions based on the user's current input.
    """

    def __init__(self, commands, corrections, ignore_case=True):
        self.commands = commands
        self.corrections = corrections
        self.ignore_case = ignore_case

    def get_completions(self, document, complete_event):
        """Generates a list of possible completions based on the user's current input."""
        word_before_cursor = document.get_word_before_cursor()
        word_lower = (
            word_before_cursor.lower() if self.ignore_case else word_before_cursor
        )
        added_commands = set()

        # Check for abbreviated versions of commands
        for correction, full_command in self.corrections.items():
            correction_lower = correction.lower() if self.ignore_case else correction
            full_command_lower = (
                full_command.lower() if self.ignore_case else full_command
            )

            if (
                full_command_lower.startswith(word_lower)
                or correction_lower.startswith(word_lower)
            ) and full_command_lower not in added_commands:

                # Display the command with its abbreviation,
                # but only insert the full command
                display_text = f"{full_command} ({correction})"
                yield Completion(
                    text=full_command,  # text that will be inserted
                    start_position=-len(word_before_cursor),
                    display=display_text,  # text displayed in the dropdown
                )
                added_commands.add(full_command_lower)

        # Add full commands if they haven't been added yet
        for cmd in self.commands:
            cmd_lower = cmd.lower() if self.ignore_case else cmd
            if cmd_lower.startswith(word_lower) and cmd_lower not in added_commands:
                yield Completion(cmd, start_position=-len(word_before_cursor))
                added_commands.add(cmd_lower)
