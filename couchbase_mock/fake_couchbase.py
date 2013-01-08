from collections import defaultdict
from fake_couchbase_bucket import FakeCouchbaseBucket


class FakeCouchbase:
    def __init__(self, host="0.0.0.0", username="user", password="couchbase"):
        self.buckets = {}

    def __getitem__(self, item):
        return self.bucket(item)

    def bucket(self, bucket_name):
        self.buckets[bucket_name] = FakeCouchbaseBucket(bucket_name)
        return self.buckets[bucket_name]

    def buckets(self, buckets):
        return self.buckets

    def create(self, bucket_name):
        self.bucket(bucket_name)
