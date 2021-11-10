import unittest
from Server import Database
from TwitterAPI import TwitterAPI, BEARER_TOKEN

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def tearDown(self):
        self.db = None

    def test_can_load_tweets(self):
        self.assertFalse()


class TestServer(unittest.TestCase):
    pass


class TestTwitterAPI(unittest.TestCase):
    def test_keyword_is_none(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url("data")
        params[0] = None
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'params' is empty")

if __name__ == '__main__':
    unittest.main()