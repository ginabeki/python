import tweepy
import time
auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# user = api.me()
# print(user.name)

# def limit_handler(cursor):
#     try:
#         while True:
#             yield cursor.next()
#     except tweepy.RateLimitError:
#         time.sleep(1000)
# # Generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
