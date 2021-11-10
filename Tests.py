import unittest
from Server import Database
from TwitterAPI import TwitterAPI, BEARER_TOKEN

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def tearDown(self):
        self.db = None

    def test_can_load_tweets(self):
        all_tweets = self.db.load_tweets()
        self.assertEqual(all_tweets, None)


class TestServer(unittest.TestCase):
    pass


class TestTwitterAPI(unittest.TestCase):
    def test_keyword_is_none(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url("data")
        params[0] = None
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'params' is empty")
    
    def test_bearer_token_not_exist(self):
        BEARER_TOKEN = ""
        headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
        url, params = TwitterAPI.create_twitter_url("data")
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: bearer token does not exist")
    
    def test_header_is_none(self):
        headers = None
        url, params = TwitterAPI.create_twitter_url('data')
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'header' is empty")



if __name__ == '__main__':
    unittest.main()