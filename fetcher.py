import json
import urllib2
import sys
import time
import json

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)



# {
#     u'kind': u't2',
#     u'data': {
#         u'has_mail': None,
#         u'name': u'rogue702',
#         u'is_friend': False,
#         u'created': 1368845691.0,
#         u'created_utc': 1368842091.0,
#         u'link_karma': 2368,
#         u'comment_karma': 15,
#         u'over_18': True,
#         u'is_gold': False,
#         u'is_mod': False,
#         u'has_verified_email': False,
#         u'id': u'bpvse',
#         u'has_mod_mail': None
#     }
# }
def parseJSON(data):
	print '------------ parsing json --------------------------------\n'	
	print 'data["kind"] = ' + data['kind']
	print 'link_karma = ' + str(data["data"]["link_karma"])

def getRedditUser(repeat, counter):
	user = 'rogue702'
	if len(sys.argv) > 1:
		print 'usage: fetcher.py username' 
		user = str(sys.argv[1])

	url = 'http://www.reddit.com/user/' + user + '/about.json'

	print '---------------------------------------- fetch(' + str(counter) +') data from url: ' + url + '\n'
	data = json.load(urllib2.urlopen(url))

	print '------------ json data --------------------------------\n'
	print data
	parseJSON(data)
	print '------------ end json data ----------------------------\n'
	if repeat == True:
		time.sleep(1)
		counter = counter + 1
		getRedditUser(repeat, counter)

getRedditUser(True, 0)