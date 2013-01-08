class FakeCouchbaseBucket:
    def __init__(self, name, server):
        self.cache = {}

    def __getitem__(self, key):
        return self.cache[key]

    def get(self, key):
        return self.__getitem__(key)

    def set(self, key, expiration, flags, value):
        self.cache[key] = value