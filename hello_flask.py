from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dsn

hello_flask = Flask(__name__)
hello_flask.config['SQLALCHEMY_DATABASE_URI'] = dsn.URI
hello_flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db is an interface for interacting with our database
db = SQLAlchemy(hello_flask)

class Person(db.Model):
    __tableName__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

db.create_all()

@hello_flask.route("/")
def hello_world():
    person = Person.query.first()
    return f"<p>Hello, {person.name}!</p>"

# running flask app option 2
if __name__=='__main__':
    hello_flask.run(host="0.0.0.0")    