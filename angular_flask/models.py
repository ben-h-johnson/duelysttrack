from datetime import datetime
from angular_flask.core import db
from angular_flask import app
from werkzeug.security import generate_password_hash, \
     check_password_hash


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, body, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return '<Post %r>' % self.title

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    pw_hash = db.Column(db.String(80))
    games = db.relationship('Game', backref='user', lazy='dynamic')
    email = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.email)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user_class = db.Column(db.String(40))
    opp_class = db.Column(db.String(40))
    win = db.Column(db.Boolean)
    date_played = db.Column(db.DateTime)

    def __init__(self, user_id, user_class, opp_class, win, date=datetime.now()):
        self.user_id = user_id
        self.user_class = user_class
        self.opp_class = opp_class
        self.win = win
        self.date_played = date

# models for which we want to create API endpoints
app.config['API_MODELS'] = {'post': Post}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {'post': Post}
