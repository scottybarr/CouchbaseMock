import unittest
from couchbase_mock.mock_couchbase import MockCouchbase
from couchbase_mock.mock_couchbase_bucket import MockCouchbaseBucket
import time


class TestFakeCouchbase(unittest.TestCase):

    def test_can_construct_fake_couchbase(self):
        fake = MockCouchbase()
        self.assertIsInstance(fake["defaults"], MockCouchbaseBucket)
        
    def test_can_get_and_set(self):
        val = "hello world!"
        fake = MockCouchbase()["bucket_name"]
        fake.set("abc", 5, 0, val)
        self.assertEqual(fake.get("abc"), val)
        self.assertGreater(fake.expiry["abc"], time.time())

    def test_item_has_expired(self):
        val = "test"
        fake = MockCouchbase()["bucket_name"]
        fake.set("tester", 1, 0, val)
        fake._get_timestamp = self.expiredTime
        self.assertDictEqual(fake.get("tester"), {})

    def test_persistant_get_item(self):
        val = "hello world!"
        fake = MockCouchbase()["bucket_name"]
        fake.set("abc", 0, 0, val)
        self.assertEqual(fake.get("abc"), val)

    def expiredTime(self):
        return time.time() * 2


if __name__ == "__main__":
    unittest.main()
