import pip._vendor.requests as requests

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAATcVAEAAAAAAt1oj%2FJgpR9pgHllTItCWBgSue0%3DZ4epJoXaPbc33YXVgznB0VenOXLqhAcxztYg4S5rZFGhZs8pE2'


class TwitterAPI:
    @staticmethod
    def create_twitter_headers():
        headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
        return headers

    @staticmethod
    def create_twitter_url(keyword, max_results=10):
        search_url = 'https://api.twitter.com/2/tweets/search/recent'

        query_params = {
            'query': keyword,
            'max_results': max_results,
            'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
            'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,'
                            'public_metrics,referenced_tweets,reply_settings,source',
            'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
            'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
            'next_token': {}
        }
        return search_url, query_params

    @staticmethod
    def query_twitter_api(url, headers, params):       
        
        
        if headers == None:
            return "Error: 'headers' is empty"  
        if not isinstance(headers,dict):
            return "Error: 'headers' is not a dict type"     
        if len(headers['Authorization']) <= 20:
            return "Error: bearer token does not exist"             
        if params['query'] == None:
            return "Error: 'data' is empty"       
        if params == None:
            return "Error: 'params' is empty"
        if not isinstance(params,dict):
            return "Error: 'params' is not a dict type"
        

        response = requests.request('GET', url, headers=headers, params=params)
        return response.json()



