import tweepy
import time
from datetime import datetime
import pytz

# Twitter API credentials
API_KEY = 'uHHXVfWFL8NDisPH2ICOtv2OR'
API_SECRET = 'tUCqWPwV3BoCH5tkEsydu6IOXB6nxmCqpMxtN1xtBBkP8aTlU6'
ACCESS_TOKEN = '1158818171240902658-QTyKTubNI5LuLy9NBeBK8vokf186oQ'
ACCESS_SECRET = '8yooKCjXMarRv4wNJ9xF1maUguQ4ZjgxX8henls32wmDG'

# Authenticate with Twitter using OAuth 1.0a for API v2
def authenticate_twitter():
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )
    return client

# Define the IST timezone
IST = pytz.timezone('Asia/Kolkata')

# Prabhas' Birthday date (October 23, 2024)
prabhas_birthday = datetime(2024, 10, 23, tzinfo=IST)

# Function to calculate remaining days until Prabhas' birthday
def days_until_birthday():
    today = datetime.now(IST)
    remaining_days = (prabhas_birthday - today).days
    print(f"Days remaining: {remaining_days}")
    return remaining_days

# Function to tweet the countdown using API v2
def tweet_birthday_countdown(client):
    print("Tweet function called!")  # Debugging
    remaining_days = days_until_birthday()

    if remaining_days > 0:
        message = f"{remaining_days} days left until Prabhas' Birthday! 🎉 #PrabhasBirthdayCountdown"
    elif remaining_days == 0:
        message = "Happy Birthday to Prabhas! 🎉 #HappyBirthdayPrabhas"
    else:
        print("Countdown complete. Stopping further tweets.")
        return

    # Try posting the tweet using API v2
    try:
        response = client.create_tweet(text=message)
        if response.data:
            print(f"Successfully tweeted: {message}")
        else:
            print(f"Failed to tweet: {response}")
    except tweepy.TweepyException as e:
        print(f"Error while tweeting: {e}")

# Manually wait until 12:00 AM IST and tweet daily
def wait_until_tweet_time():
    client = authenticate_twitter()

    while True:
        now = datetime.now(IST)
        print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')} IST")  # Debugging

        # If the current time is exactly 12:00 AM, tweet
        if now.hour == 0 and now.minute == 0:
            tweet_birthday_countdown(client)
            print("Tweet posted at 12:00 AM IST")

            # Wait until the next day
            print("Waiting until the next day...")
            time.sleep(60)  # Wait for 60 seconds to avoid multiple posts within the same minute

            # Sleep until the next 12:00 AM
            while True:
                now = datetime.now(IST)
                if now.hour == 0 and now.minute == 0:
                    break
                time.sleep(60)

        # Check every minute
        time.sleep(60)

if __name__ == "__main__":
    wait_until_tweet_time()
# import tweepy
# import time
# from datetime import datetime
# import pytz
#
# # Twitter API credentials
# API_KEY = 'uHHXVfWFL8NDisPH2ICOtv2OR'
# API_SECRET = 'tUCqWPwV3BoCH5tkEsydu6IOXB6nxmCqpMxtN1xtBBkP8aTlU6'
# ACCESS_TOKEN = '1158818171240902658-QTyKTubNI5LuLy9NBeBK8vokf186oQ'
# ACCESS_SECRET = '8yooKCjXMarRv4wNJ9xF1maUguQ4ZjgxX8henls32wmDG'
#
# # Authenticate with Twitter using OAuth 1.0a for API v2
# def authenticate_twitter():
#     client = tweepy.Client(
#         consumer_key=API_KEY,
#         consumer_secret=API_SECRET,
#         access_token=ACCESS_TOKEN,
#         access_token_secret=ACCESS_SECRET
#     )
#     return client
#
# # Define the IST timezone
# IST = pytz.timezone('Asia/Kolkata')
#
# # Prabhas' Birthday date (October 23, 2024)
# prabhas_birthday = datetime(2024, 10, 23, tzinfo=IST)
#
# # Function to calculate remaining days until Prabhas' birthday
# def days_until_birthday():
#     today = datetime.now(IST)
#     remaining_days = (prabhas_birthday - today).days
#     print(f"Days remaining: {remaining_days}")
#     return remaining_days
#
# # Function to tweet the countdown using API v2
# def tweet_birthday_countdown(client):
#     print("Tweet function called!")  # Debugging
#     remaining_days = days_until_birthday()
#
#     if remaining_days > 0:
#         message = f"{remaining_days} days left until Prabhas' Birthday! 🎉 #PrabhasBirthdayCountdown"
#     elif remaining_days == 0:
#         message = "Happy Birthday to Prabhas! 🎉 #HappyBirthdayPrabhas"
#     else:
#         print("Countdown complete. Stopping further tweets.")
#         return
#
#     # Try posting the tweet using API v2
#     try:
#         response = client.create_tweet(text=message)
#         if response.data:
#             print(f"Successfully tweeted: {message}")
#         else:
#             print(f"Failed to tweet: {response}")
#     except tweepy.TweepyException as e:
#         print(f"Error while tweeting: {e}")
#
# # Manually tweet without waiting for 12:00 AM for testing purposes
# def wait_until_tweet_time():
#     client = authenticate_twitter()
#
#     # Tweet immediately for testing
#     tweet_birthday_countdown(client)
#     print("Tweet posted immediately for testing.")
#
# if __name__ == "__main__":
#     wait_until_tweet_time()
