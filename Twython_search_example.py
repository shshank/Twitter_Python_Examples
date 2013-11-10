from twython import Twython
#make sure you have twython module installed "pip install twython"


#Enter your search term, no. of tweets, and auth details below
hashtag = ''
cnt = 10
cons_key = ''
cons_secret = ''
access_key = ''
access_token = ''

twitter = Twython(cons_key, cons_secret, access_key, access_token)

search_result = twitter.search(q=hashtag, count=cnt)
statuses = search_result['statuses']

def learn_structure():
    print "\n\nThis is what a search result will contain\n These is all the raw data in Dictionary structure. We will go through each of them in detail."
    for key in search_result:
        print "*** %s ***\n %s \n\n" %(key, search_result[key])

    print "\n--------\nMetadata is the information about your search result\n"
    metadata = search_result['search_metadata']
    for key in metadata:
        print " %s : %s \n" %(key, metadata[key])
 
    print "\n--------\nStatuses contain the actual search results. We got %s statuses. Lets see how one of them looks like.\n" %(cnt)
    status = statuses[0]
    for key in status:
        print "* %s : %s \n" %(key, status[key])

    print "\n\n--------\nYou saw that status object has a user key. Lets see what user object looks like.\n"
    user = status['user']
    for key in user:
        print "* %s : %s \n" %(key, user[key])

print "\n\n--------\nNow lets see all the %s tweets::::\n" %(cnt)
for tweet in statuses:
    print "At %s, @%s said:: %s\n" %(tweet['created_at'], tweet['user']['screen_name'], tweet['text'])
    
#to learn about how the search results are structured uncomment the next line.
#learn_structure()
