import re


def safefind(pattern: str, string: str, index: int) -> str:
    try:
        return re.findall(pattern, string)[index]
    except IndexError:
        return ""


def rreplace(s, old, new, occurrence):
    """https://stackoverflow.com/a/2556252"""
    li = s.rsplit(old, occurrence)
    return new.join(li)
