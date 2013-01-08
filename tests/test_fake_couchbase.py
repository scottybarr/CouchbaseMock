import unittest
from couchbase_mock.fake_couchbase import FakeCouchbase
from couchbase_mock.fake_couchbase_bucket import FakeCouchbaseBucket


class TestFakeCouchbase(unittest.TestCase):

    def test_can_construct_fake_couchbase(self):
        fake = FakeCouchbase()
        self.assertIsInstance(fake["defaults"], FakeCouchbaseBucket)
        
    def test_can_get_and_set(self):
        val = "hello world!"

        fake = FakeCouchbase()["bucket_name"]
        fake.set("abc", 5, 0, val)
        self.assertEqual(fake.get("abc"), val)


if __name__ == "__main__":
    unittest.main()
