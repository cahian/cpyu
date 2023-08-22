from collections.abc import Iterator


class GlobalCounter:
    def __init__(self):
        self.start = {}
        self.counter = {}
        self.last_key = None

    def get(self, parentkey, key, start):
        self.start[key] = start
        self.counter[key] = start
        while True:
            if self.last_key == parentkey:
                self.counter[key] = start
            value = self.counter[key]
            self.counter[key] += 1
            self.last_key = key
            yield value

    def restore(self):
        self.counter[self.last_key] -= 1

    def reset(self):
        for key, value in self.start.items():
            self.counter[key] = value 


class SafeCounterItem:
    def __init__(self, start):
        self.value = start
        self.reset = False


class SafeCounter:
    def __init__(self):
        self.values = {}

    def count(self, key: str, start: int) -> Iterator[int]:
        if not key in self.values:
            self.values[key] = start
        while True:
            yield self.values[key]
            self.values[key] += 1

    def reset(self, key: str = None):
        if key:
            del self.values[key]
        else:
            self.values = {}
