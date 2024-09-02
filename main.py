import os
import client_api as ca
import auth_api as aa
import tweet_functions as tf

api_key = os.environ['API KEY']
api_secret = os.environ['API KEY SECRET']
bearer_token = os.environ['BEARER TOKEN']
access_token = os.environ['ACCESS TOKEN']
access_token_secret = os.environ['ACCESS TOKEN SECRET']

client = ca.clientapi(bearer_token,api_key,api_secret,access_token,access_token_secret)

api = aa.apiauth(api_key,api_secret,access_token,access_token_secret)

print('1. Create Tweet')
print('2. Like the tweet')
print('3. Retweet')
print('4. Display Tweets')
print('5. Get tweets of an account')
user_input = int(input('Enter the function you want to perform:\n'))

tf.tweetfunctions(user_input,client,api)