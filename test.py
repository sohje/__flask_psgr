import os
from app import app
from app import init_db
import unittest
import json

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True # propogate exceptions
        self.app = app.test_client()

    def tearDown(self):
        pass

    def testRootEndPoint(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 404)

    def testProfilesEndPointUnAuth(self):
        res = self.app.get('/api/v1/profiles/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(type(data), type({}))
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['Message'], 'Invalid session')

    def testProfilesEndPointAuth(self):
        res = self.app.get('/api/v1/profiles/1?session=1')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(type(json.loads(res.data)), type({}))

        data = json.loads(res.data)
        self.assertEqual(data['user_id'], 1)
        self.assertEqual(data['sex'], 'M')
        self.assertEqual(data['city'], 'Kanzas')
        self.assertEqual(data['country'], 'USA')
        self.assertEqual(data['name'], 'Jack')

    def testSelfProfileEndPointUnAuth(self):
        res = self.app.get('/api/v1/profiles/self')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(type(data), type({}))
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['Message'], 'Invalid session')

    def testSelfProfileEndPointAuth(self):
        res = self.app.patch(
            '/api/v1/profiles/self?session=1',
            data=json.dumps({"sex": "F", "city": 'Tokyo', "country": "Japan"}),
            headers={'content-type':'application/json'}
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(type(data), type({}))
        self.assertEqual(data['status'], 'OK')

        # test self profile endpoint after patch
        res = self.app.get('/api/v1/profiles/1?session=1')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(type(data), type({}))

        self.assertEqual(data['user_id'], 1)
        self.assertEqual(data['sex'], 'F')
        self.assertEqual(data['country'], 'Japan')
        self.assertEqual(data['city'], 'Tokyo')
        self.assertEqual(data['name'], 'Jack')

if __name__ == '__main__':
    unittest.main()
