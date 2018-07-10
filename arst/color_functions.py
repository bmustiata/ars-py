from termcolor import colored


def yellow(text: str, bold=False) -> str:
    attrs = ["bold"] if bold else None
    return colored(text, color="yellow", attrs=attrs)


def red(text: str, bold=False) -> str:
    attrs = ["bold"] if bold else None
    return colored(text, color="red", attrs=attrs)


def cyan(text: str, bold=False) -> str:
    attrs = ["bold"] if bold else None
    return colored(text, color="cyan", attrs=attrs)
