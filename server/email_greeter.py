# This is the email greeter service - you will need to get a message into here
# which is then parsed and inserted into the db as appopriate

import hashlib
import simplejson as json
import re


import get_email

exlude_filters = ['Re:', 'Fwd:']
regc = re.compile('(re:|fwd:)')


# this is what email obj should look like - ideally
email_obj = {
    'to': ['text@example.com', 'test2@example.com'], 
    'from': ['me@example.com'], 
    'subject' : 'Email subject line',
    'content' : 'Content',
    'thread_id' : ''
    }

def process_subject(subj):
    """gets raw subject and returns the normalized version"""
    # todo: smarter normalization
    return ''


def process_email(email):
    # todo: remove the re  / fwd stuff from the subj
    cleaned_subj = process_subject(email['subject'])

def do_poll():
    """Poll the message server and process the results"""
    msgs = get_email.get_messages()
    print msgs


def start():
    """docstring for start"""
    do_poll()


if __name__ == '__main__':
    start()
