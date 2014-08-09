# -*- coding: utf-8 -*-
"""yopy: Zero characters communication for humans.
"""
from __future__ import print_function
import sys

import requests
from slugify import slugify

YO_ALL_URL = 'http://api.justyo.co/yoall/”'
YO_SEND_URL = 'http://yofor.me'

class YoError(Exception):
    pass

class ErrorResponse(Exception):
    def __init__(self, message=None, status_code=None):
        self.status_code = status_code
        Exception.__init__(self, message or 'An error occurred with the Yo API.')

def format_as_yo_username(s):
    return slugify(s.strip().upper(), separator='_')

class Yo(object):

    def __init__(self, user=None, token=None):
        self.user = user
        self.token = token
        self._session = requests.Session()

    def yo_all(self):
        """Send a yo to all subscribers. Requires API key."""
        if not self.token:
            raise YoError('yo_all requires an api token.')
        resp = self._session.post(YO_ALL_URL, data={'api_token': self.token})
        if resp.status_code >= 400:
            raise ErrorResponse(resp.json().get('message'), resp.status_code)
        return resp

    def yo(self, to, from_=None):
        """Send a yo. Does not require an API key.

        :param str to: Username of recipient.
        :param str from_: Username of sender.
        """
        fr = from_ or self.user
        if not fr:
            raise YoError('Sender not specified.')
        to_formatted = format_as_yo_username(to)
        fr_formatted = format_as_yo_username(fr.strip())
        url = '{base}/{to}/{fr}'.format(
            base=YO_SEND_URL,
            to=to_formatted,
            fr=fr_formatted
        )
        resp = self._session.post(url)
        if resp.status_code >= 400:
            raise ErrorResponse(resp.json().get('message'), resp.status_code)
        return resp

def main():
    if len(sys.argv) != 3:
        print('Usage: yopy <to> <from>', file=sys.stderr)
        sys.exit(1)
    to, from_ = sys.argv[1], sys.argv[2]
    try:
        print('...')
        Yo().yo(to, from_)
    except ErrorResponse as err:
        print('ERROR {}: {}'.format(err.status_code, err), file=sys.stderr)
        sys.exit(1)
    print("Yo'd.")
    sys.exit(0)

if __name__ == '__main__':
    main()
