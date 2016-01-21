# TopPostOnVoat - Twitter Bot - Tweets the current top post on voat.co/v/all

from twython import Twython, TwythonError
import time
import GetTopPost

KEYS = [line.rstrip('\n') for line in open('/home/pi/TopPostOnVoat/keys.txt')]
LOG = open('/home/pi/TopPostOnVoat/log.txt', 'a')

# twitter keys/authentification tokens
APP_KEY = KEYS[0]
APP_SECRET = KEYS[1]
OAUTH_TOKEN = KEYS[2]
OAUTH_TOKEN_SECRET = KEYS[3]

twitter_api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Returns post content
status = GetTopPost.main()

if status != 'null':
    # Post content to Twitter
    twitter_api.update_status(status=status)
    # Write success msg to log file
    LOG.write('TPOV - Successful Post @ ' + time.ctime() + '\n')
else:
    # Write error msg to log file
    LOG.write('TPOV - ERROR: Duplicate Post @ ' + time.ctime() + '\n')

