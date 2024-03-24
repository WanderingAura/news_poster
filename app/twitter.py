import tweepy
from keys import CONSUMER_PK, CONSUMER_SK, TOKEN_PK, TOKEN_SK

class Twitter:
    """
    A class creating an interface to the tweepy library which is itself an interface to the twitter API
    """
    def __init__(self) -> None:
        """
        Initialises the v2 and v1.1 twitter API. self.client is v2, self.api is v1.1
        """
        self.client = tweepy.Client(
            consumer_key=CONSUMER_PK,
            consumer_secret=CONSUMER_SK,
            access_token=TOKEN_PK,
            access_token_secret=TOKEN_SK,
        )

        auth = tweepy.OAuth1UserHandler(CONSUMER_PK, CONSUMER_SK)
        auth.set_access_token(TOKEN_PK, TOKEN_SK)
        self.api = tweepy.API(auth)
    
    def post(self, text):
        self.client.create_tweet(text=text)

    def get_home_timeline(self):
        return self.api.home_timeline()