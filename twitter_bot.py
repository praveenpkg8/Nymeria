import requests
import json

from urllib.parse import urlencode





tweet_id_data = open("data.json", "r")
tweet_id = json.load(tweet_id_data)
tweet_id_json = json.dump(tweet_id)



Authorization = "Bearer {}".format(access_token)
headers = {"Authorization": Authorization}
query_params = urlencode({ "q": "#100DaysOfCode -filter:retweets AND -filter:replies"})

endpoint_url = "https://api.twitter.com/1.1/search/tweets.json"
response = requests.get(url=endpoint_url,params=query_params,headers=headers)
search_tweets = json.loads(response.text)
with open("data.json", "w") as json_file:
    json.dump(search_tweets,json_file)
# tweets_list = search_tweets.get('statuses')
# for tweets in tweets_list:
#     print(tweets.get("text"))

