import requests
import json
from urllib.parse import urlencode


class AuthService(object):

    @staticmethod
    def generate_access_token(credentials):
        auth_url = "https://api.twitter.com/oauth2/token"
        api_file = open("twitter_api_key.json", "r")
        data = json.load(api_file)
        api_file.close()
        response = requests.post(
            auth_url,
            data=data,
            verify=False,
            allow_redirects=False,
            auth=(data.get('api_key'), data.get('api_secret_key')))

        response_data = json.loads(response.text)
        access_token = response_data.get("access_token")

        # TODO: add access token to db


class TweetService(object):

    @staticmethod
    def retweet_tweet_by_id(tweet_id):
        pass

    @staticmethod
    def fetch_tweets():
        # TODO: get access token from db

        access_token = ""
        Authorization = "Bearer {}".format(access_token)
        headers = {"Authorization": Authorization}
        query_params = urlencode({"q": "#100DaysOfCode -filter:retweets AND -filter:replies"})
        endpoint_url = "https://api.twitter.com/1.1/search/tweets.json"
        response = requests.get(url=endpoint_url, params=query_params, headers=headers)
        search_tweets = json.loads(response.text)

        # TODO: store tweets in DB and remove

    @staticmethod
    def retweet_tweets():
        #
