from my_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "vivishigexiaotaiyang"
TWITTER_PASSWORD = "vivishigexiaotaiyang"
USERNAME = "vivishigexiaotaiyang"

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()

input("Press Enter when you have solved the Captcha")

twitter_bot.tweet_at_provider(PROMISED_DOWN, PROMISED_UP, TWITTER_EMAIL, TWITTER_PASSWORD,  USERNAME)