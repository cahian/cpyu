import os

TERMCOLORS = os.environ.get("TERMCOLORS") != "0"


def bold(s: str) -> str:
    return f"\033[1m{s}\033[0m" if TERMCOLORS else s


def fail(s: str) -> str:
    return s
    # return f"\033[91m{s}\033[91m" if TERMCOLORS else s
