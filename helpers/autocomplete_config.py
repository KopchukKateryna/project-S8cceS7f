from prompt_toolkit.key_binding import KeyBindings
from constants import COMMAND_CORRECTIONS
from constants import COMMAND_FOR_EDIT_CONTACT


bindings = KeyBindings()


@bindings.add("enter")
def _(event):
    buffer = event.current_buffer
    input_text = buffer.text.strip()

    if input_text in COMMAND_CORRECTIONS:
        buffer.text = COMMAND_CORRECTIONS[input_text]

    if buffer.complete_state and buffer.complete_state.current_completion:
        buffer.apply_completion(buffer.complete_state.current_completion)
    else:
        event.app.exit(result=buffer.text)


bindings_for_contact = KeyBindings()


@bindings_for_contact.add("enter")
def _(event):
    buffer = event.current_buffer
    input_text = buffer.text.strip()

    if input_text in COMMAND_FOR_EDIT_CONTACT:
        buffer.text = COMMAND_FOR_EDIT_CONTACT[input_text]

    if buffer.complete_state and buffer.complete_state.current_completion:
        buffer.apply_completion(buffer.complete_state.current_completion)
    else:
        event.app.exit(result=buffer.text)
