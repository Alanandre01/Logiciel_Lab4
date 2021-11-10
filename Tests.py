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
    
    def test_can_save_tweets(self):
        self.db.save_tweets(["tweet"])
        self.assertEqual(len(self.db.tweets), 0)


class TestServer(unittest.TestCase):
    pass


class TestTwitterAPI(unittest.TestCase):
    def test_params_is_none(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url("data")
        params = None
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
        self.assertEqual(json_response, "Error: 'headers' is empty")

    def test_header_not_dict_type(self):
        headers = int(1234)
        url, params = TwitterAPI.create_twitter_url('data')
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'headers' is not a dict type")

    def test_params_not_dict_type(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url('data')
        params = int(1234)
        json_response = TwitterAPI.query_twitter_api(url, headers, params)       
        self.assertEqual(json_response, "Error: 'params' is not a dict type")
    
    def test_data_is_none(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url(None)
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'data' is empty")

    def test_data_not_string_type(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url(int(1234))
        json_response = TwitterAPI.query_twitter_api(url, headers, params)       
        self.assertEqual(json_response, "Error: 'data' is not a string type")

if __name__ == '__main__':
    unittest.main()