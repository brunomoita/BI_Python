import tweepy
from tweepy import OAuthHandler

consumer_key = "1Bkcpy9yoLfeQTN2CNUOO55NH"
consumer_secret = "h0iVHrEeZfHYp9Fdf0VkUk3AnU0v6nGvQjgnraPlkdf2ivlePC"
access_token = "62681172-DENZBaTjRXrt1GVM17KC2j8wemqLnnpoU7BqMuvU9"
access_token_secret = "VWQUMrQCxoiLVgXDislhZZVqYDptD189AiGgcD5AnQbC6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

keyword = "brunomoita"
tweets = api.search(keyword, count=10, lang='en', exclude='retweets',
                    tweet_mode='extended')
for item in tweets:
    print(item)