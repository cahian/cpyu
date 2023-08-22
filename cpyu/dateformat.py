from datetime import datetime

from dateutil.relativedelta import relativedelta

from .text import lowerstrcmp


def convert(datestring: str, fromformat: str, toformat: str) -> str:
    return datetime.strptime(datestring, fromformat).strftime(toformat)


def delta(date_string: str, fmt: str, **step):
    new_date = datetime.strptime(date_string, fmt) + relativedelta(**step)
    return new_date.strftime(fmt)


def gettoday(format):
    return datetime.today().strftime(format)

# pt-br
def getmonthnumber(monthname):
    if lowerstrcmp(monthname, "janeiro"):
        return 1
    if lowerstrcmp(monthname, "fevereiro"):
        return 2
    if lowerstrcmp(monthname, "março"):
        return 3
    if lowerstrcmp(monthname, "abril"):
        return 4
    if lowerstrcmp(monthname, "maio"):
        return 5
    if lowerstrcmp(monthname, "junho"):
        return 6
    if lowerstrcmp(monthname, "julho"):
        return 7
    if lowerstrcmp(monthname, "agosto"):
        return 8
    if lowerstrcmp(monthname, "setembro"):
        return 9
    if lowerstrcmp(monthname, "outubro"):
        return 10
    if lowerstrcmp(monthname, "novembro"):
        return 11
    if lowerstrcmp(monthname, "dezembro"):
        return 12
    return -1
