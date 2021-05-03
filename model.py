"""Data model file"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    """A user."""

    __tablename__ = "recipients"

    recipient_id = db.Column(db.Integer,
                             autoincrement=True,
                             primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.DateTime)
    address = db.Column(db.String)
    email = db.Column(db.String)

    def __repr__(self):
        return f'<Recipient name={self.name} birthday={self.birthday}>'


def setup_tables():
    db.create_all()

    test_recipient = Recipient(name="Sarah",
                               birthday=(datetime.utcnow()), address="123 Elm Street", email="sarah1@test.com")
    db.session.add(test_recipient)

    db.session.commit()


if __name__ == '__main__':

    connect_to_db(app)
    setup_tables()
