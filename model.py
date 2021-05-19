"""Data model file"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = "dev"


def connect_to_db(flask_app, db_uri='postgresql:///gift-tracker', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


class Recipient(db.Model):
    """A gift receiver."""

    __tablename__ = "recipients"

    recipient_id = db.Column(db.Integer,
                             autoincrement=True,
                             primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date)
    address = db.Column(db.String)
    email = db.Column(db.String)

    def __repr__(self):
        return f'<Recipient name={self.name} birthday={self.birthday}>'


class Event(db.Model):
    __tablename__ = "events"

    event_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    category = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Event name={self.name} date={self.date} category={self.category}>'


def setup_tables():
    db.create_all()

    test_recipient = Recipient(name="Sarah",
                               birthday=date.today(), address="123 Elm Street", email="sarah1@test.com")

    test_event = Event(name="Christmas", date=(
        "2019, 12, 4"), category="holiday")
    db.session.add(test_recipient)
    db.session.add(test_event)

    db.session.commit()


if __name__ == '__main__':

    connect_to_db(app)
    setup_tables()
