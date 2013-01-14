CouchbaseMock
=============

A mock couchbase class to be used for python unit tests.

Setup:
```
pip install -r requirements.txt
```

Usage:
```
fake = MockCouchbase()["bucket_name"]
fake.set('key', 60, 0, "value")
fake.get('key') # returns "value"
```

Running The tests:
```
nosetests
```