import praw
import re
import time
import random

#Access to Reddit's API requires OAuth2 creditials which are obtained when you register 'client_id and client_secrets'
reddit = praw.Reddit(client_id= 'ScfP4NVD7_sRNw',
				client_secret= "beIKb5OvO6dT1LapbUPfxec6q0v35Q", 
				user_agent='<console: DOPEBOT:1.0>',
				username= 'dope_boot',
				password= "GET_YOUR_OWN")

love_ravens = ["Not bad for a running back. -Lamar Jackson",
'Anytime somebody tells me I can’t do something, I’m going to do it. -Lamar Jackson', 
"There was one school that stood by my side…That was the University of Louisville. -Lamar Jackson", 
"Just an honor for the Ravens organization to believe in me. And all the teams that passed me up … there’s a lot that’s gonna come with that. -Lamar Jackson" ]
hate_ravens = ["Ray Lewis is the best to ever do it", "Ed Reed is the best to ever do it", "Ravens need this win", "This is our year", "Lamar Jackson is only getting better", 'JK all the way',
 'Jimmy Smith', "We going Hollywood", "Ravens all the way!!!", "PLAYOFFS Babyyyyy"]

we_the_best = love_ravens + hate_ravens


#subreddit r/ravens   
subreddit = reddit.subreddit('ravens')
# iterating through subreddit 'ravens' popular post Hot attribute and printing the title of those post.
for post in subreddit.hot(limit=10):
	# print('.............')
	# print(post.title)
#iterating through comments of subreddit
	for comment in post.comments:
		#if comment has attribute hasattr() return if not don't 
		if hasattr(comment, 'body'):
			comment_lower = comment.body.lower()
			if 'love' in comment_lower:
				print('................')
				print(comment.body)
				random_index = random.randint(0, len(we_the_best) -1)
				'''func to randomly select a quote from the love_ravens list'''

				comment.reply(we_the_best[random_index])
				'''replying to subreddit comments'''
				 
				time.sleep(540)
				'''time delay 10 min so we don't look like a bot just speeding through comments'''

		


		
