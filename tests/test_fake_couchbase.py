import unittest
from couchbase_mock.mock_couchbase import MockCouchbase
from couchbase_mock.mock_couchbase_bucket import MockCouchbaseBucket


class TestFakeCouchbase(unittest.TestCase):

    def test_can_construct_fake_couchbase(self):
        fake = MockCouchbase()
        self.assertIsInstance(fake["defaults"], MockCouchbaseBucket)
        
    def test_can_get_and_set(self):
        val = "hello world!"

        fake = MockCouchbase()["bucket_name"]
        fake.set("abc", 5, 0, val)
        self.assertEqual(fake.get("abc"), val)


if __name__ == "__main__":
    unittest.main()
