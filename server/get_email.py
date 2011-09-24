import imaplib
from pprint import pprint
import os


def open_connection():
    # Connect to the server
    hostname = 'imap.mailgun.org'
    print 'Connecting to', hostname
    connection = imaplib.IMAP4_SSL(hostname)

    # Login to our account
    username = 'mumbo@mumbo.mailgun.org'
    password = 'jumbo11'
    print 'Logging in as', username
    connection.login(username, password)
    return connection


def get_inboxes():
    c = open_connection()
    try:
        typ, data = c.list()
        print 'Response code:', typ
        print 'Response:'
        pprint(data)
    finally:
        c.logout()



import email
def get_message():
    """docstring for get_message"""
    c = open_connection()
    try:
        c.select('INBOX', readonly=True)
        
        typ, msg_data = c.fetch('1', '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                for header in [ 'subject', 'to', 'from' ]:
                    print '%-8s: %s' % (header.upper(), msg[header])

    finally:
        try:
            c.close()
        except:
            pass
        c.logout()







if __name__ == '__main__':
    get_inboxes()
    get_message()
