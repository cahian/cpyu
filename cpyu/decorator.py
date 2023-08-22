import functools
import inspect


def onlyext(ext):
    if "." not in ext:
        ext = "." + ext

    def decorator(func):
        @functools.wraps(func)
        def wrapper(filename, *args, **kwargs):
            if filename.endswith(ext):
                return func(filename, *args, **kwargs)
            return ""

        return wrapper

    return decorator


def exceptionsafe(*exceptions, limit=None):
    if not limit:
        limit = dict()

    exceptions = list(exceptions)
    for i, e in enumerate(exceptions):
        if inspect.isclass(e):
            exceptions[i] = e.__name__
    for k, v in list(limit.items()):
        if inspect.isclass(k):
            limit[k.__name__] = limit.pop(k)

    def decorator(func):
        counter = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                try:
                    func(*args, **kwargs)
                    break
                except Exception as e:
                    name = e.__class__.__name__
                    if name in exceptions:
                        if name not in counter:
                            counter[name] = 1
                        else:
                            counter[name] += 1
                        if counter[name] == limit.get(name, 10):
                            print(f"**DEBUG: exceptionsafe: {name}: Exception limit exceeded!**")
                            break
                        else:
                            print(f"DEBUG: exceptionsafe: {name}: {counter[name]}")
                        ###
                        # import traceback
                        # print(traceback.format_exc())
                        ###
                    else:
                        raise e

        return wrapper

    return decorator


onlytxt = onlyext("txt")
onlyzip = onlyext("zip")
onlyxls = onlyext("xls")
