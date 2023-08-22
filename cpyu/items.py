from operator import itemgetter


def getitems(object, *items):
    return itemgetter(*items)(object)


def has_duplicates(object):
    return len(object) != len(set(object))
