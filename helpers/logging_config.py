import logging
import colorlog

DETAILED_LOG_COLORS = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "bold_red",
}
SIMPLE_LOG_COLORS = {
    "DEBUG": "green",
    "INFO": "cyan",
    "WARNING": "yellow",
    "ERROR": "white",
    "CRITICAL": "bold_red",
}


def setup_logging(format_type="detailed", logger_name=None):
    """
    Set up colored logging for the application with flexible formatting.

    Parameters:
    - format_type: str, either "detailed" or "simple". Determines the log format.
    - logger_name: str, the name of the logger. If None, root logger is used.
    """
    logger = colorlog.getLogger(logger_name)

    if logger.hasHandlers():
        logger.handlers.clear()

    handler = colorlog.StreamHandler()

    format_msg = (
        "%(log_color)s%(asctime)s - %(levelname)s - %(message)s"
        if format_type == "detailed"
        else "%(log_color)s%(message)s"
    )
    log_colors = DETAILED_LOG_COLORS if format_type == "detailed" else SIMPLE_LOG_COLORS

    formatter = colorlog.ColoredFormatter(
        format_msg,
        datefmt=None,
        reset=True,
        log_colors=log_colors,
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


debug_logger = setup_logging(format_type="detailed", logger_name="command_logger")
command_logger = setup_logging(format_type="simple", logger_name="debug_logger")


def custom_print(logger, message, space="both", level="info", **kwargs):
    """
    Universal function for colorized message output with a flexible logger.

    Parameters:
    - logger: the logger object for outputting messages.
    - message: the message string.
    - space: str, either "both", "top", "bottom", or "none".
    - level: the logging level ("debug", "info", "warning", "error", "critical").
    - **kwargs: a dictionary where the key is a word in the message,
    and the value is the color of that word.
    """
    color_codes = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m",
        "bold": "\033[1m",
        "underline": "\033[4m",
        "blink": "\033[5m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
        "bright_white": "\033[97m",
    }

    log_color = {
        "debug": color_codes["green"],
        "info": color_codes["cyan"],
        "warning": color_codes["yellow"],
        "error": color_codes["red"],
        "critical": f"{color_codes['bold']}{color_codes['red']}",
    }.get(level.lower(), color_codes["reset"])

    # Replacing keywords in the message with their colorized versions
    for placeholder, value in kwargs.items():
        if isinstance(value, tuple) and len(value) == 2:
            color, text = value
            if color in color_codes:
                colored_text = f"{color_codes[color]}{text}{log_color}"
                message = message.replace(f"{{{placeholder}}}", colored_text)
        else:
            color = value
            if color in color_codes:
                colored_text = f"{color_codes[color]}{placeholder}{log_color}"
                message = message.replace(f"{{{placeholder}}}", colored_text)

    if space == "top" or space == "both":
        print()

    if level.lower() == "debug":
        logger.debug(message)
    elif level.lower() == "info":
        logger.info(message)
    elif level.lower() == "warning":
        logger.warning(message)
    elif level.lower() == "error":
        logger.error(message)
    elif level.lower() == "critical":
        logger.critical(message)
    else:
        logger.info(message)

    if space == "bottom" or space == "both":
        print()


if __name__ == "__main__":
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("black", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("red", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("green", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("yellow", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("blue", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("magenta", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("cyan", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("reset", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("bold", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("underline", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("blink", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("bright_yellow", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("bright_blue", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("bright_magenta", "Enter note name: "),
    )
    custom_print(
        command_logger,
        "{msg}",
        level="info",
        msg=("bright_cyan", "Enter note name: "),
    )
# custom_print(
#     command_logger,
#     "{This} is an {important} message",
#     level="info",
#     **{"important": "green", "This": "magenta"},
# )
# custom_print(
#     debug_logger, "This is an {important} message", level="info", important="green"
# )
# custom_print(
#     debug_logger,
#     "Command executed: {edit-contact bob}",
#     level="debug",
#     **{"edit-contact bob": "blue"},
# )
# custom_print(
#     debug_logger,
#     "Success: {Data saved successfully}",
#     level="info",
#     **{"Data saved successfully": "yellow"},
# )
# custom_print(
#     debug_logger,
#     "Failure: {Unable to connect to server}",
#     level="error",
#     **{"Unable to connect to server": "red"},
# )
