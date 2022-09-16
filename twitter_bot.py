import tweepy, openai, random, time, schedule
#import list as list_of_words
#API key and secret in Twitter Developer account

list_of_people = [
]


def reply(username, tweet,tweet_id):
    response = openai.Completion.create(
    engine = "text-davinci-001",
    prompt = "a sarcastic tweet response to "+tweet,
    max_tokens = 64
    )
    output = response.choices[0].text
    api.create_favorite(tweet_id)
    api.update_status(output,in_reply_to_status_id = tweet_id , auto_populate_reply_metadata=True)


def post(api_key, api_secret, access_key, access_secret, openai_key):
    openai.api_key =  openai_key

    #api info from twitter developer account
    authentication = tweepy.OAuthHandler(api_key, api_secret)
    authentication.set_access_token(access_key,access_secret)
    api = tweepy.API(authentication)

    chosen_prompt = random.choice(list_of_people)

    response = openai.Completion.create(
    engine = "text-davinci-001",
    prompt = "a motivational quote by "+chosen_prompt+ "with quotations,their name, and 5 motivational hashtags",
    max_tokens = 64
    )
    output = response.choices[0].text
    api.update_status(output)

#twitter api information from Twitter Developer account
api_key = ""
api_secret = ""

#Access key and secret from Twitter Developer account
access_key = ""
access_secret = ""

#OpenAI info
openai_key = ""
openai.api_key =  openai_key

#api info from twitter developer account
authentication = tweepy.OAuthHandler(api_key, api_secret)
authentication.set_access_token(access_key,access_secret)
api = tweepy.API(authentication)

post(api_key, api_secret, access_key, access_secret, openai_key)

#user name    
user = ""
limit = 7
actual_tweet = "none"
actual_tweet_id = 0
tweets = tweepy.Cursor(api.user_timeline,screen_name = user,count = 200,tweet_mode = 'extended').items(limit)
for tweet in tweets:
    if tweet.full_text[0] != "R" and tweet.full_text[1] != "T":
        if tweet.full_text[0]!= "@":
            actual_tweet = tweet.full_text
            actual_tweet_id = tweet.id
            reply(user,actual_tweet,actual_tweet_id)
            
   

