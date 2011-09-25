	# -*- coding: utf-8 -*-
"""
    xerox
    ~~~~~

    Blueprint example application.

    :copyright: (c) 2011 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    """
    renders the index page template
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run()