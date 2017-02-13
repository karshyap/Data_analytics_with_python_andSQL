import tweepy
import os
import datetime
from datetime import date
from scipy.stats import  itemfreq
import matplotlib.pyplot as plt
import ggplot
from ggplot import *

print(os.getcwd())
consumerKey = 'BfWnwt59p9r6Ix7xb7c0igVpM'
consumerSecret = 'lcTrg8xIt7di8hv5IKrXQQutPYA0YfZA1CeGs1DBT8e9xrgU6E'
accessToken = '194530798-k3tL28zxYoirmH8eYfTH1UvwuZBQDr2mySQoBPeR'
accessTokenSecret = 'BOtCtPs2mBUnEwEujZZcLsJ4EeUMJbLJXsXhhL4IJZRDu'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

username='realDonaldTrump'

startDate = datetime.datetime(2016, 4, 1, 0, 0, 0)
endDate =   datetime.datetime(2017, 2, 10, 0, 0, 0)

tweets = []


tmpTweets = api.user_timeline(username,count=200)

if(1):
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet.created_at.date())
    
    while (tmpTweets[-1].created_at > startDate and len(tweets)<3200):

        tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id,count=200)
        for tweet in tmpTweets:
            if tweet.created_at < endDate and tweet.created_at > startDate:
                tweets.append(tweet.created_at.date())

tweets_uniq=itemfreq(tweets)
x_axis_data=[]
y_axis_data=[]
for i in range(1,len(tweets_uniq)):
    x_axis_data.append(i)
    y_axis_data.append(tweets_uniq[i][1])

fig, ((ax1)) = plt.subplots(1, 1, sharex='col', sharey='row')

plt.style.use('ggplot')
plt.plot(x_axis_data,y_axis_data,lw=3)
plt.xlabel("Number of Days from March 31", fontsize=15,fontweight='bold')
plt.ylabel("Number of tweets per day", fontsize=15,fontweight='bold')
plt.title("Donald Trump's tweet Histogram",fontsize=25,fontweight='bold')

ax1.tick_params(axis='x', labelsize=20)
ax1.tick_params(axis='y', labelsize=20 )


plt.grid(color='w',lw=6)
plt.show()