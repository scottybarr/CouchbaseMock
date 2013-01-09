import time

class MockCouchbaseBucket:
    def __init__(self, name, server):
        self.cache = {}
        self.expiration = {}

    def __getitem__(self, key):
        self._checkExpiry(key)
        return self.cache[key] if key in self.cache else {}

    def get(self, key):
        return self.__getitem__(key)

    def set(self, key, expiration, flags, value):
        self.expiration[key] = 0 if expiration == 0 else (self._getTimeStamp() + expiration)
        self.cache[key] = value

    def _checkExpiry(self, key):
        currentTime = self._getTimeStamp()
        if self.expiration[key] and self.expiration[key] < currentTime and self.expiration[key] != 0:
            del self.cache[key]
            del self.expiration[key]

    def _getTimeStamp(self):
        return time.time()