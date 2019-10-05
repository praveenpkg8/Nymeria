import requests
import json

from urllib.parse import urlencode

url = "https://api.twitter.com/oauth2/token"
retweet_url = "https://api.twitter.com/1.1/statuses/retweet/1177602818741374976"

api_file = open("twitter_api_key.json", "r")
data = json.load(api_file)
api_file.close()
r = requests.post(
    url,
    data=data,
    verify=False,
    allow_redirects=False,
    auth=(data.get('api_key'), data.get('api_secret_key')))


# tweet_id_data = open("data.json", "r")
# tweet_id = json.load(tweet_id_data)
# tweet_id_json = json.dump(tweet_id)

response_data = json.loads(r.text)
access_token = response_data.get("access_token")

Authorization = "Bearer {}".format(access_token)
headers = {"Authorization": Authorization}
# query_params = urlencode({"id": "1177602818741374976"})
#
# response = requests.post(
#     retweet_url,
#     params=query_params,
#     headers=headers,
# )
# print(response.text)


query_params = urlencode({ "q": "#100DaysOfCode -filter:retweets AND -filter:replies"})



endpoint_url = "https://api.twitter.com/1.1/search/tweets.json"
response = requests.get(url=endpoint_url, params=query_params,headers=headers)
search_tweets = json.loads(response.text)
with open("data.json", "w") as json_file:
    json.dump(search_tweets, json_file)
tweets_list = search_tweets.get('statuses')
for tweets in tweets_list:
    print(tweets.get("text"))

