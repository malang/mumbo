from app import app

if __name__ == "__main__":
    app.debug = True
    app.run()


from flask import Flask, session, g, render_template