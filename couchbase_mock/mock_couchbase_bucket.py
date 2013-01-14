import time


class MockCouchbaseBucket:
    def __init__(self, name, server):
        self.cache = {}
        self.expiry = {}
        self.views = {}

    def __getitem__(self, key):
        self._check_expiry(key)
        return self.cache[key] if key in self.cache else {}

    def get(self, key):
        return self.__getitem__(key)

    def set(self, key, expiration, flags, value):
        self.expiry[key] = 0 if not expiration else self._get_timestamp(expiration)
        self.cache[key] = value

    def view(self, view, **options):
        return self.views[view]

    def set_views(self, views):
        self.views = views

    def _check_expiry(self, key):
        currentTime = self._get_timestamp()
        if self.expiry[key] and self.expiry[key] < currentTime and self.expiry[key] != 0:
            del self.cache[key]
            del self.expiry[key]

    def _get_timestamp(self, added_time=0):
        return time.time() + added_time
