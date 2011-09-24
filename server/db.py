# This is the email greeter service - you will need to get a message into here
# which is then parsed and inserted into the db as appopriate

# This is the db layer where we will make the db calls
import pymongo
from pymongo import Connection

def _return_conn():
    return pymongo.Connection().mumbo

def write_thread(client, key, emobj):
    """ 
    client: 
    key: normalized subj
    emboj: the email obj
    """
    db = _return_conn()
    db.test.insert({"x": "y", "a": "b"})


if __name__ == '__main__':
    write_thread({})


