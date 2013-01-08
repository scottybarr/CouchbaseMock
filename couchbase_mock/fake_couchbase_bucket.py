class FakeCouchbaseBucket:
    def __init__(self, bucket_name):
        self.cache = {}

    def __getitem__(self, item):
        pass