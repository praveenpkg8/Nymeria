import json
import time
from logging.config import dictConfig
import threading

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

from flask import Flask

from bot_services import AuthService, TweetService

app = Flask(__name__)


@app.route("/auth", methods=["GET"])
def get_access_token():
    credentials = json.load(open("twitter_api_key.json"))
    AuthService.generate_access_token(credentials=credentials)
    return json.dumps({"message": "Access token created successfully"})


@app.route("/tweet", methods=["GET"])
def get_tweets():
    tweet_result = TweetService.fetch_tweets()
    return json.dumps(tweet_result)

def foo():
    print(time.ctime())

def beat():
    ticker = threading.Event()
    while not ticker.wait(2):
        foo()



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    # heart_beat = threading.Thread(target=beat)
    # heart_beat.start()
