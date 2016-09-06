#!/usr/bin/env python

from twitter import *

accts = get_all_accounts()

try:
	tweet = raw_input("Tweet: \n")
	if len(tweet) > 140:
		print("Tweet exceeds character count by " + len(tweet)-140 + ".")
	else:
		post_tweet(accts[0], tweet)
except:
	pass
