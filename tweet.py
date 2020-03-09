import twitter

try:
    import configparser
except ImportError as _:
    import ConfigParser as configparser

import getopt
import os
import sys

'''
Make sure you provide valid credentials in the .tweetrc file
Usage : python tweet.py your awesome tweet
'''
class TweetRc(object):
    def __init__(self):
        self._config = None

    def GetConsumerKey(self):
        return self._GetOption('consumer_key')

    def GetConsumerSecret(self):
        return self._GetOption('consumer_secret')

    def GetAccessKey(self):
        return self._GetOption('access_key')

    def GetAccessSecret(self):
        return self._GetOption('access_secret')

    def _GetOption(self, option):
        try:
            return self._GetConfig().get('Tweet', option)
        except:
            return None

    def _GetConfig(self):
        if not self._config:
            self._config = configparser.ConfigParser()
            self._config.read(os.path.expanduser('./.tweetrc'))
        return self._config

def main():
    rc = TweetRc()
    consumer_key = rc.GetConsumerKey()
    consumer_secret = rc.GetConsumerSecret()
    access_key = rc.GetAccessKey()
    access_secret = rc.GetAccessSecret()

    args = sys.argv[1:]
    message = ' '.join(args)

    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token_key=access_key, access_token_secret=access_secret,)

    status = api.PostUpdate(message)
    print("{0} just posted: {1}".format(status.user.name, status.text))


if __name__ == "__main__":
    main()