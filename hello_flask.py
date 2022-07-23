from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dsn

hello_flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dsn.URL
db = SQLAlchemy(app)

@hello_flask.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# running flask app option 2
# if __name__=='__main__':
#     hello_flask.run(host="0.0.0.0")    