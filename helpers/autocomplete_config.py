from prompt_toolkit.key_binding import KeyBindings
from constants import COMMAND_CORRECTIONS
from constants import COMMAND_FOR_EDIT_CONTACT
from constants import COMMAND_FOR_ADD_EDIT_DELETE
from constants import COMMAND_FOR_EDIT_DELETE
from constants import COMMAND_FOR_NAME_TEXT


def create_enter_handler(command_corrections):
    """
    Creates an enter key handler that applies command corrections
    based on the provided corrections dictionary.

    Parameters:
    ----------
    command_corrections : dict
        A dictionary where the keys are incorrect commands and the values
        are the corrected commands.

    Returns:
    -------
    function
        A function to be used as a key binding handler.
    """

    def enter_handler(event):
        buffer = event.current_buffer
        input_text = buffer.text.strip()

        if input_text in command_corrections:
            buffer.text = command_corrections[input_text]

        if buffer.complete_state and buffer.complete_state.current_completion:
            buffer.apply_completion(buffer.complete_state.current_completion)
        else:
            event.app.exit(result=buffer.text)

    return enter_handler


bindings_general = KeyBindings()
bindings_for_contact = KeyBindings()
bindings_for_notes = KeyBindings()
bindings_for_add_edit_delete = KeyBindings()
bindings_for_edit_delete = KeyBindings()
bindings_for_name_text = KeyBindings()

bindings_general.add("enter")(create_enter_handler(COMMAND_CORRECTIONS))
bindings_for_contact.add("enter")(create_enter_handler(COMMAND_FOR_EDIT_CONTACT))
bindings_for_add_edit_delete.add("enter")(create_enter_handler(COMMAND_FOR_ADD_EDIT_DELETE))
bindings_for_edit_delete.add("enter")(create_enter_handler(COMMAND_FOR_EDIT_DELETE))
bindings_for_name_text.add("enter")(create_enter_handler(COMMAND_FOR_NAME_TEXT))
# bindings_for_notes.add("enter")(create_enter_handler(________))
