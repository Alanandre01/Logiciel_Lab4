import pip._vendor.requests as requests

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAATcVAEAAAAAAt1oj%2FJgpR9pgHllTItCWBgSue0%3DZ4epJoXaPbc33YXVgznB0VenOXLqhAcxztYg4S5rZFGhZs8pE2"


class TwitterAPI:
    @staticmethod
    def create_twitter_headers():
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
        return headers

    @staticmethod
    def create_twitter_url(keyword, max_results=10):
        search_url = "https://api.twitter.com/2/tweets/search/recent"

        if keyword == "":
            print("Error: 'data' is empty")
        query_params = {
            "query": keyword,
            "max_results": max_results,
            "expansions": "author_id,in_reply_to_user_id,geo.place_id",
            "tweet.fields": "id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,"
            "public_metrics,referenced_tweets,reply_settings,source",
            "user.fields": "id,name,username,created_at,description,public_metrics,verified",
            "place.fields": "full_name,id,country,country_code,geo,name,place_type",
            "next_token": {},
        }
        return search_url, query_params

    @staticmethod
    def query_twitter_api(url, headers, params):

        # headers
        if headers == None:
            return "Error: 'headers' is empty"
        if not isinstance(headers, dict):
            return "Error: 'headers' must be a dict type"
        
        # params
        if params == None:
            return "Error: 'params' is empty"
        if not isinstance(params, dict):
            return "Error: 'params' must be a dict type"
        
        # data
        if params["query"] == None:
            return "Error: 'data' is empty"
        if params["query"] == "":
            return "Error: 'data' is empty"
        if not isinstance(params["query"], str):
            return "Error: 'data' must be a string type"
        
        # bearer_token
        if not isinstance(headers["Authorization"], str):
            return "Error: 'BEARER_TOKEN' must be a string type"
        if len(headers["Authorization"]) <= 20:
            return "Error: bearer token does not exist"
        
        # url
        if not isinstance(url, str):
            return "Error: 'url' must be a string type"
        if len(url) == 0:
            return "Error: 'url' is empty"
        
        # max_result
        if params["max_results"] == None:
            return "Error: 'max_results' is empty"
        if not isinstance(params["max_results"], int):
            return "Error: 'max_results' must be an int type"
        if params["max_results"] < 10:
            return "Error: 'max_results' must be greater than 10"
        if params["max_results"] > 100:
            return "Error: 'max_results' must be less than 100"
        
        response = requests.request("GET", url, headers=headers, params=params)
        return response.json()
