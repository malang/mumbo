from flask import Flask
from flask import render_template
import pymongo
from pymongo import Connection
import email

def _return_conn():
    return pymongo.Connection().mumbo

def read_single_thread(key):
    """
    gets a single thread info
    """
    db = _return_conn()
    thread = {}
    thread['replies'] = db.test.find({'thread': key}).count()
    #get the last email of the thread
#    thread['thread'] =  db.test.find({'thread': key, 'msg': 0})
    #thread['date'] = db.test.find({'thread': key, 'msg': msg})
    # email_str = db.test.find( {'thread': key} ).sort( {'id':-1} ).limit(1)
    t = db.test.find_one( {'thread': key} )
    
    thread['subject'] = t['msg']['Subject']
    thread['last_date'] = t['msg']['Date'].replace(',','')[0:6]
    return thread

app = Flask(__name__)

@app.route("/")
def index():
    """
    renders the index page template
    """
    db = _return_conn()
    
    # get all the threads
    all_threads = db.test.distinct('thread')
    
    threads = []
    for key in all_threads:
        threads.append(read_single_thread(key))
        
    username = 'asdf'

    return render_template('index.html', username=username, threads=threads)