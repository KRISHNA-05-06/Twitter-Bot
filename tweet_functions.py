def createtweet(client,tweet):
    client.create_tweet(text=tweet)

def liketweet(client,tweetid):
    client.like(tweetid)

def retweet(client,tweetid):
    client.retweet(tweetid)
    tweettext = input('Enter the text you want to retweet:\n')
    client.create_tweet(in_reply_to_tweet_id = tweetid,text = tweettext)

def displaytweets(api):
    for tweet in api.home_timeline():
        print(tweet.text)

def gettweets(client,person):
    for tweet in client.get_users_tweets(person).data:
        print(tweet.data)

def tweetfunctions(user_input,client,api):
    if user_input == 1:
        tweet = input('Enter tweet you want to post:\n')
        createtweet(client,tweet)
    elif user_input == 2:
        tweetid = int(input('Enter tweet id which you want to like:\n'))
        liketweet(client,tweetid)
    elif user_input == 3:
        tweetid = int(input('Enter tweet id which you want to like:\n'))
        retweet(client,tweetid)
    elif user_input == 4:
        displaytweets(api)
    elif user_input == 5:
        uname = input('Enter username of the account:\n')
        person = client.get_user(username = uname).data.id
        gettweets(client,person)