import tweepy
from tokens import get_twitter_creds


def post_to_twitter(image_path, post_caption,):
    creds = get_twitter_creds()
    auth = tweepy.OAuthHandler(
        creds["twitter_consumer_key"], creds["twitter_consumer_secret"])
    auth.set_access_token(creds["twitter_access_token"],
                          creds["twitter_access_token_secret"])
    api = tweepy.API(auth)
    tweet_text = post_caption
    api.update_with_media(image_path, tweet_text)
