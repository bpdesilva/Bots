from twython import Twython, TwythonError

#Get this data from https://apps.twitter.com/
app_key = "YOUR_APP_KEY"
app_secret = "YOUR_APP_SECRET"
oauth_token = "YOUR_OAUTH_TOKEN"
oauth_token_secret = "YOUR_OAUTH_TOKEN_SECRET"

removed_words = [" -RT", "removed", "eliminated", "leaked", "cancer"] #Remove these words
real_words = ["goasksef", "sef", "sustainable education foundation"] #Search from these
filter = " OR ".join(real_words)
blacklist = " -".join(removed_words)
keywords = filter + blacklist

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

search_results = twitter.search(q=keywords, count=10)
try:
    for tweet in search_results["statuses"]:
        try:
            twitter.retweet(id = tweet["id_str"])
        except TwythonError as e:
            print e
except TwythonError as e:
    print e
