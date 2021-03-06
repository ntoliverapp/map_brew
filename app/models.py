from re import S
from sqlalchemy import desc, asc
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_urlsafe

from sqlalchemy.ext.declarative import declarative_base
db.Base = declarative_base()

def generate_token():
    return token_urlsafe(20)

def generate_hash(token):
    return generate_password_hash(token)

def _check_token(hash, token):
    return check_password_hash(hash, token)

class Remember(db.Model):
    __tablename__ = "remember"

    id            = db.Column(db.Integer(), primary_key=True)
    remember_hash = db.Column(db.String(255), nullable=False)
    user_id       = db.Column(db.Integer(), db.ForeignKey("user.id"), index=True, nullable=False)

    def __init__(self, user_id):
        self.token         = generate_token()
        self.remember_hash = generate_hash(self.token)
        self.user_id       = user_id

    def check_token(self, token):
        return _check_token(self.remember_hash, token)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Boolean, nullable=False)
    password      = db.Column(db.String(255), nullable=False)
    remember_hashes    = db.relationship("Remember", backref="user", lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, username="", email="", password="", age=""):
        self.username         = username
        self.email            = email
        self.password    = generate_password_hash(password)
        self.age              = age

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def passwords(self):
        raise AttributeError("Password should not be read like this")

    @passwords.setter
    def passwords(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return not "" == self.username

    def is_anonymous(self):
        return "" == self.username

    def get_remember_token(self):
        remember_instance = Remember(self.id)
        db.session.add(remember_instance)
        return remember_instance.token

    def check_remember_token(self, token):
        if token:
            for remember_hash in self.remember_hashes:
                if remember_hash.check_token(token):
                    return True
        return False

    def forget(self):
        self.remember_hashes.delete()

    @staticmethod
    def newest(num):
        return User.query.order_by(desc(User.username)).limit(num)
    
    @staticmethod
    def display(num):
        return User.query.order_by(asc(User.username)).limit(num)
    
class Style(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    source = db.Column(db.Text)
    image_url = db.Column(db.Text)
    
    @staticmethod
    def displays():
        return Style.query.order_by(asc(Style.name)).all()
    
    @staticmethod
    def style_filter():
        return Style.query.order_by(asc(Style.name)).all()
    
    @staticmethod
    def sub_page():
        return Style.query.order_by(asc(Style.name))
    
class Beer(db.Model):
    __tablename__ = "beer"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    styles = db.Column(db.String(100))
    brewery = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(25))
    description = db.Column(db.Text)
    abv = db.Column(db.Text)
    min_ibu = db.Column(db.Text)
    max_ibu = db.Column(db.Text)
    astringency = db.Column(db.String(25))
    body = db.Column(db.String(25))
    alcohol = db.Column(db.String(25))
    bitter = db.Column(db.String(25))
    sweet = db.Column(db.String(25))
    sour = db.Column(db.String(25))
    salty = db.Column(db.String(25))
    fruits = db.Column(db.String(25))
    hops = db.Column(db.String(25))
    spices = db.Column(db.String(25))
    malts = db.Column(db.String(25))
    aroma = db.Column(db.String(25))
    appearance = db.Column(db.String(25))
    palate = db.Column(db.String(25))
    taste = db.Column(db.String(25))
    overall = db.Column(db.String(25))
    image_url = db.Column(db.Text)
    style_id = db.Column(db.Integer, db.ForeignKey('style.id'))
    
    @staticmethod
    def newest(num):
        return Beer.query.order_by(asc(Beer.name)).limit(num)
    
    @staticmethod
    def display(num):
        return Beer.query.order_by(desc(Beer.name)).limit(num)
    
    
    @staticmethod
    def search_results():
        return Beer.query.order_by(asc(Beer.name)).all()
    
    @staticmethod
    def sub_pages():
        return Beer.query.order_by(asc(Beer.name))
    
    def __Repr__(self):
        return "<Beer '{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}'{}''{}'>".format(self.name, self.style, self.brewery, self.city, self.state, self.description, self.abv, self.min_ibu, self.max_ibu, self.astringency, self.body, self.alcohol, self.bitter, self.sweet, self.sour, self.salty, self.fruits, self.hops, self.spices, self.malts, self.aroma, self.appearance, self.palate, self.taste, self.overall, self.image_url)

class SavedBeers (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    beer_id = db.Column(db.Integer, db.ForeignKey('beer.id'))
