import requests
import logging
import json

from urllib.parse import urlencode


from utils.helper import get_auth_headers

LOG = logging.getLogger(__name__)

class AuthService(object):

    @staticmethod
    def generate_access_token(credentials):

        token_url = "https://api.twitter.com/oauth2/token"
        data = credentials
        response = requests.post(
            token_url,
            data=data,
            verify=False,
            allow_redirects=False,
            auth=(data.get('api_key'), data.get('api_secret_key')))
        response_data = json.load(response.text)
        access_token = response_data.get("access_token", None)

        #TODO: create DB and store access token


class TweetService(object):

    @staticmethod
    def fetch_tweets():

        headers = get_auth_headers()
        query_params = urlencode({ "q": "#100DaysOfCode -filter:retweets AND -filter:replies"})
        fetch_tweets_url = "https://api.twitter.com/1.1/search/tweets.json"
        response = requests.get(
            url=fetch_tweets_url,
            params=query_params,
            headers=headers
        )
        tweet_result = json.load(response.text)
        tweet_list = tweet_result.get("statuses")

        #TODO: push it to task queue for retweet

    @staticmethod
    def retweet_by_id(tweet_id):
        query_params = {"id": tweet_id}
        headers = get_auth_headers()
        retweet_url = "https://api.twitter.com/1.1/statuses/retweet/1177602818741374976"
        response = requests.post(
            retweet_url,
            params=query_params,
            headers=headers
        )
        if response.status_code == 200:
            LOG.info("retweeted tweet => {}".format(tweet_id))
