# This is the email greeter service - you will need to get a message into here
# which is then parsed and inserted into the db as appopriate

import hashlib
import simplejson as json
import re
import db

import get_email

exlude_filters = ['Re:', 'Fwd:']
regc = re.compile('(re:|fwd:)', flags=re.I)


# this is what email obj should look like - ideally
email_obj = {
    'to': ['text@example.com', 'test2@example.com'], 
    'from': ['me@example.com'], 
    'subject' : 'Email subject line',
    'content' : 'Content',
    'thread_id' : ''
    }

# ['Content-Type', 'MIME-Version', 'Received', 'Received', 'Dkim-Signature', 
#  'Received', 'Received', 'From', 'Date', 'Message-Id', 'Subject', 'To']

def process_subject(subj):
    """gets raw subject and returns the normalized version"""
    subj = subj.strip()
    return re.sub(regc, '', subj).strip()

def process_email(email):
    # todo: remove the re / fwd stuff from the subj
    cleaned_subj = process_subject(email['subject'])
    print cleaned_subj

def do_poll():
    """Poll the message server and process the results"""
    drop = ['Dkim-Signature', ]
    msgs = get_email.get_messages()
    for msg in msgs:
        topheaders = ['To', 'From', 'Message-Id', 'Date']
        msgobj = dict([(x,msg[x]) for x in topheaders])
        
        print('Message subject %s' %msg['Subject'])
        print('Message date %s' %msg['Date'])
        subjkey = process_subject(msg['Subject'])
        msgobj['Subject'] = subjkey
        msgobj['Content'] = msg.as_string()
       
        print subjkey
        db.write_thread(subjkey, msgobj)

    # print [msg.keys() for msg in msgs]


def start():
    """docstring for start"""
    db.reset()
    do_poll()


if __name__ == '__main__':
    start()
