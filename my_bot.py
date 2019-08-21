import tweepy
from tweepy import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
import time
from random import randint

#i don't want to give ouy my api keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

#defining replys
#users would be replaced with actual twitter accounts
reply0 = " @user1 @user2 @user3 @user4 @user5 check this one out"
reply1 = " @user2 @user5 @user6 @user7 @user8 look at this one"
reply2 = " @user3 @user2 @user1 @user8 @user4 jump on this one lads"
reply3 = " @user4 @user1 @user3 @user6 @user7 done"
reply4 = " @user3 @user2 @user1 @user8 @user4 let's test our luck boys"
reply5 = " @user1 @user7 @user6 @user8 @user4 check it out boys"

#authenticate application
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

class listener(StreamListener):
    def on_status(self, status):
        try:
            tweet_text = status.text.lower()
            tweet_id = status.id
            attributes = getattr(status, 'retweeted_status', None)

            if attributes is not None:
                screen_name = status.retweeted_status.author.screen_name
            else:
                screen_name = status.author.screen_name

            #if things aren't working I can try printing things

            #banned accounts
            accs = [] #ex: 'username'

            #banned words
            bad_words = ["i entered", "i entered to win a", "i'm entered to win a", "check out and follow", "you can enter here too", "go", "- go", "gleam.io", "i just entered", "i am in the running", "i'm in the running"]

            #target words
            retweet_words = ["retweet", " rt", "rt", "re-tweeted", "re-tweet", "#retweet", "#rt", "#re-tweeted", "#re-tweet"]
            fav_words = ["favorite", "like", "fav", "fave", "#favorite", "#like", "#fav", "#fave"]
            follow_words = ["followed", "follow", "#followed", "#follow", "flw", "#flw"]

            if not any(acc in screen_name.lower() for acc in accs):
                if not any(word in tweet_text for word in bad_words):
                    if any(word in tweet_text for word in retweet_words):
                        retweet_words(tweet_id)
                    if any(word in tweet_text for word in fav_words):
                        fav(tweet_id)
                    if any(word in tweet_text for word in follow_words):
                        follow(tweet_id)
                    if "done" in tweet_text:
                        api.update_status(str('@' + screen_name + 'done'), in_reply_status_id = tweet_id)
                    if "tag" in tweet_text:
                        random_number = randint(0,5)
                        if random_number == 0:
                            api.update_status(str('@' + screen_name + reply0), in_reply_status_id == tweet_id)
                        if random_number == 1:
                            api.update_status(str('@' + screen_name + reply1), in_reply_status_id == tweet_id)
                        if random_number == 2:
                            api.update_status(str('@' + screen_name + reply2), in_reply_status_id == tweet_id)
                        if random_number == 3:
                            api.update_status(str('@' + screen_name + reply3), in_reply_status_id == tweet_id)
                        if random_number == 4:
                            api.update_status(str('@' + screen_name + reply4), in_reply_status_id == tweet_id)
                        if random_number == 5:
                            api.update_status(str('@' + screen_name + reply5), in_reply_status_id == tweet_id)
                    #avoid making too many requests
                    time.sleep(60*5)
                    return True
        except Exception as e:
            print(str(e))
            pass

    def on_limit(self, track):
        print 'limit hit! track = %s' % track
        return

    def on_error(self, status):
        print 'an error has occured! status code = %s' % status
        return True

    def on_timeout(self):
        print 'timeout... zzzzzzzzzz'
        return

def fav(tweet_cid):
    try:
        api.create_favorite(tweet_cid)
    except Exception as e:
        print('cout not favorite tweet ' + str(e))
        pass

def retweet(tweet_cid):
    try:
        api.retweet(tweet_cid)
    except Exception as e:
        print('could not retweet tweet ' + str(e))
        pass

def follow(screen_name):
    try:
        api.create_friendship(screen_name)
    except Exception as e:
        print('could not follow user' + str(e))
        pass

def unfav(tweet_cid)
    try:
        api.destroy_favorite(tweet_cid)
    except Exception as e:
        print('could not unfavorite tweet ' + str(e))
        pass

def tweet(my_input)
    try:
        api.update_status(my_input)
    except Exception as e:
        print('could not tweet ' + str(e))
        pass

#not working
def tri_followers():
    try:
        for following in api.followers():
            if not api.exists_friendship(following, self):
                api.destroy_friendship()
    except Exception as e:
        print('could not trim follows ' + str(e))
        pass

track_words = "#giveaway"
follow_acc = []

try:
    twitter_stream = Stream(auth, listener())
    twitter_stream.filter(track = track_words, follow = follow_acc)
except Exception as e:
    print('could not start stream ' + str(e))
    pass
