from couchbase_mock.fake_couchbase_bucket import FakeCouchbaseBucket


class FakeCouchbase:
    def __init__(self, host="0.0.0.0", username="user", password="couchbase"):
        self.buckets = {}

    def __getitem__(self, key):
        return self.bucket(key)

    def bucket(self, bucket_name):
        self.buckets[bucket_name] = FakeCouchbaseBucket(bucket_name, self)
        return self.buckets[bucket_name]

    def buckets(self):
        return self.buckets

    def create(self, bucket_name, bucket_password='', ram_quota_mb=100, replica=0):
        self.bucket(bucket_name)
