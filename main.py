import tweepy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Twitter API credentials from your .env file

access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token=os.getenv("BEARER_TOKEN")
api_key=os.getenv("API_KEY")
api_secret=os.getenv("API_SECRET")

client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

client.create_tweet(text="hi");



