import json
import urllib2
import sys
import time
import json

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)



def getRedditUser(repeat, counter):
	user = 'rogue702'
	if len(sys.argv) > 1:
		print 'usage: fetcher.py username' 
		user = str(sys.argv[1])

	url = 'http://www.reddit.com/user/' + user + '/about.json'

	print '---------------------------------------- fetch(' + str(counter) +') data from url: ' + url + '\n'
	data = json.load(urllib2.urlopen(url))
	print data

getRedditUser(True, 0)