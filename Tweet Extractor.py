import tweepy
import csv
####input your credentials here
consumer_key = 'MI7pxEATg67wXtbdZ04P01zic'
consumer_secret = 'mzjofKvCNHbVnAAZEQTzZFrliEKkvF05GNgFZSioDC9Wp752cW'
access_token = '1215780002-2fC55jHbZ4X7NDHgKFJMO1g63Aw0jn1zdmhJjs8'
access_token_secret = 'MJfwXrZ9hKvfb8EUba7eoKlu5BIPDwRDKAXHZOBPdPc2p'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('newdemon.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Demonetisation",lang="en").items():
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.retweet_count,tweet.favorite_count,tweet.retweeted,tweet.lang])