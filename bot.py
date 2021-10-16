import tweepy 
import datetime 
consumer_key = 'TIL10ds3pmGPpI7LkJ0j8U5t8' 
consumer_secret = 'hUjGyf7MceneL971COIwNY02LdhSqTQx9nizFSa2muU7XnA1Qc' 
access_token = '1439635409235972097-XSkj76AE2v7r5xCmmeihpj7dQ6k9gI' 
access_token_secret = 'AlhJufo3NiKzbOdVHukHXf9c0CShPBhDBweboLNCbtnAs' 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def publictweet():
    tweettopublish = 'Hi everyone, today is '+str(datetime.date.today().weekday()+1)+"th day of LocalHackDay . Happy Hacking :)  @MLHacks, @NathanDimmer . Tweeted by bot created by Ajmal"
    api.update_status(tweettopublish)
    print(tweettopublish)
    

publictweet()