import twitter
#make sure you have python-twitter module installed "pip install python-twitter"
#enter you auth details
cons_key = ''
cons_secret = ''
access_key = ''
access_secret = ''

api=twitter.Api(consumer_key=cons_key, consumer_secret=cons_secret, 
access_token_key=access_key, access_token_secret=access_secret)

timelines = []

users = api.GetFriends()

for item in users:  
    print item.name  
    timelines.append(api.GetUserTimeline(item.id))
print timelines