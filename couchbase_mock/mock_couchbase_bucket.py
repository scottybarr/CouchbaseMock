import time


class MockCouchbaseBucket:
    def __init__(self, name, server):
        self.cache = {}
        self.expiry = {}

    def __getitem__(self, key):
        self._checkExpiry(key)
        return self.cache[key] if key in self.cache else {}

    def get(self, key):
        return self.__getitem__(key)

    def set(self, key, expiration, flags, value):
        self.expiry[key] = 0 if not expiration else self._getTimeStamp(expiration)
        self.cache[key] = value

    def _checkExpiry(self, key):
        currentTime = self._getTimeStamp()
        if self.expiry[key] and self.expiry[key] < currentTime and self.expiry[key] != 0:
            del self.cache[key]
            del self.expiry[key]

    def _getTimeStamp(self, added_time=0):
        return time.time() + added_time
