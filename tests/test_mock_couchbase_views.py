import unittest
from couchbase_mock.mock_couchbase import MockCouchbase


class TestMockCouchbaseViews(unittest.TestCase):

    def setUp(self):
        self.mock_db = MockCouchbase()["bucket_name"]
        self.views = {
            'places' : {
                'Europe': {
                    'UK': {
                        'Scotland': 'Edinburgh',
                        'England': 'London'
                    }
                }
            }
        }
        self.mock_db.set_views(self.views)

    def test_can_get_view(self):
        places = self.mock_db.view('places')
        self.assertEqual(places['Europe']['UK']['Scotland'], 'Edinburgh')


if __name__ == "__main__":
    unittest.main()
