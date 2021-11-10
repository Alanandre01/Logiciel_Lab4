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
        self.assertEqual(json_response, "Error: 'headers' must be a dict type")

    def test_params_not_dict_type(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url('data')
        params = int(1234)
        json_response = TwitterAPI.query_twitter_api(url, headers, params)       
        self.assertEqual(json_response, "Error: 'params' must be a dict type")
    
    def test_data_is_none(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url(None)
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'data' is empty")

    def test_data_not_string_type(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url(int(1234))
        json_response = TwitterAPI.query_twitter_api(url, headers, params)       
        self.assertEqual(json_response, "Error: 'data' must be a string type")

    def test_bearer_token_not_string_type(self):
        headers = {'Authorization': int(1234)}
        url, params = TwitterAPI.create_twitter_url('data')
        json_response = TwitterAPI.query_twitter_api(url, headers, params)    
        self.assertEqual(json_response, "Error: 'BEARER_TOKEN' must be a string type")

    def test_url_is_none(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url('data')
        url = ''
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'url' is empty")
    
    def test_url_not_string_type(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url('data')
        url = int(1234)
        json_response = TwitterAPI.query_twitter_api(url, headers, params)       
        self.assertEqual(json_response, "Error: 'url' must be a string type")

    def test_data_is_empty(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url('')
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'data' is empty")
    
    def test_max_results_is_none(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url('data', None)
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'max_results' is empty")

    def test_max_results_not_int_type(self):
        headers = TwitterAPI.create_twitter_headers()
        max_results = str("abcd")
        url, params = TwitterAPI.create_twitter_url('data',max_results)
        json_response = TwitterAPI.query_twitter_api(url, headers, params)       
        self.assertEqual(json_response, "Error: 'max_results' must be an int type")

    def test_max_results_is_less_than_10(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url('data', 9)
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'max_results' must be greater than 10")

    def test_max_results_is_greater_than_100(self):
        headers = TwitterAPI.create_twitter_headers()
        url, params = TwitterAPI.create_twitter_url('data', 101)
        json_response = TwitterAPI.query_twitter_api(url, headers, params)
        self.assertEqual(json_response, "Error: 'max_results' must be less than 100")

if __name__ == '__main__':
    unittest.main()