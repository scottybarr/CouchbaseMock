import unittest
from couchbase_mock.fake_couchbase import FakeCouchbase
from couchbase_mock.fake_couchbase_bucket import FakeCouchbaseBucket


class TestFakeCouchbase(unittest.TestCase):

    def test_can_construct_fake_couchbase(self):
        fake = FakeCouchbase()
        self.assertIsInstance(fake["defaults"], FakeCouchbaseBucket)


if __name__ == '__main__':
    unittest.main()
