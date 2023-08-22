import itertools
from datetime import datetime

from dateutil.relativedelta import relativedelta


def retry(times: int = 10):
    for i in range(times):
        yield i + 1


def groupby(iterable, keyfunc):
    sorted_iterable = sorted(iterable, key=keyfunc)
    for key, group in itertools.groupby(sorted_iterable, key=keyfunc):
        yield key, list(group)


def rangedate(start, stop, *, fmt="%Y%m", **step):
    datestart = datetime.strptime(start, fmt)
    datestop = datetime.strptime(stop, fmt)

    date = datestart
    while date != datestop:
        yield date.strftime(fmt)
        date += relativedelta(**step)
