from flask import Flask, redirect
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

    # the following is the string representation for the object class Person
    def __repr__(self):
        return 'User id => {0} name {1}'.format(self.id, self.name)

db.create_all()

@hello_flask.route("/")
def hello_world():
    person = Person.query.first()
    return f"<p>Hello, {person.name}!</p>"

@hello_flask.route("/newUser")
def newUser(name="User"):
    id = len(Person.query.all()) + 1
    p = Person(id=id, name=name)
    db.session.add(p)
    db.session.commit()
    for person in Person.query.all():
        print(f"<Person ID: {person.id}, Name: {person.name}")
    return redirect("/")
# running flask app option 2
if __name__=='__main__':
    hello_flask.run(host="0.0.0.0")    