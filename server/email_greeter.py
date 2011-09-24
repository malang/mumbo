# This is the email greeter service - you will need to get a message into here
# which is then parsed and inserted into the db as appopriate

import hashlib
import simplejson as json
import re

exlude_filters = ['Re:', 'Fwd:']
re.compile('(re:|fwd:)')


# this is what email obj should look like - ideally
email_obj = {
    'to': ['text@example.com', 'test2@example.com'], 
    'from': ['me@example.com'], 
    'subject' : 'Email subject line',
    'content' : 'Content'
    'thread_id': ''
    }

def process_subject(subj):
    """gets raw subject and returns the normalized version"""
    # todo: smarter normalization
    return ''


def process_email(email):
    # todo: remove the re  / fwd stuff from the subj
    cleaned_subj = process_subject(email['subject'])

