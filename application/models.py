from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime as dt


class User(UserMixin, db.Model):
    """Data model for user accounts"""

    __tablename__ = "user_accounts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=False, unique=False, nullable=False)
    username = db.Column(db.String(50), index=True, unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(50), index=False, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    in_game = db.Column(db.Boolean, index=False, unique=False, nullable=False)
    games_created = db.relationship('Battle', backref='owner', lazy=True)
    games_joined = db.relationship('Player', backref='user', lazy=True)


    def set_password(self, password):
        """Create password hash"""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check password hash"""
        return check_password_hash(self.password, password)

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def create_battle(self):
        new_battle = Battle(owner_id=self.id, round_number=1, time_created=dt.now())
        self.in_game = True
        db.session.add(new_battle)
        db.session.commit()
        new_battle = Battle.query.filter(Battle.owner_id==self.id).order_by(Battle.time_created.desc()).first()
        new_player = Player(battle_id=new_battle.id, user_id=self.id, user_status="Alive", time_created=dt.now())
        db.session.add(new_player)
        db.session.commit()

    def change_status(self):
        self.in_game = not self.in_game
        db.session.commit()

    def __repr__(self):
        return '<Username {}>'.format(self.username)

class Battle(db.Model):
    """Data Model for battle data"""

    __tablename__ = "battles"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user_accounts.id'), nullable=False)
    round_number = db.Column(db.Integer, index=False, unique=False, nullable=False)
    winner_id = db.Column(db.Integer, index=False, unique=False, nullable=True)
    time_created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    time_ended = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def __repr__(self):
        return '<Battle_id {}>'.format(self.id)


class Player(db.Model):
    """Data Model for Players in the battle"""

    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    battle_id = db.Column(db.Integer, db.ForeignKey('battles.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_accounts.id'), nullable=False)
    user_status = db.Column(db.String(10), index=False, unique=False, nullable=False)
    time_created = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def __repr__(self):
        return '<Player_id {}>'.format(self.id)


class Move(db.Model):
    """Data Model to store the players' moves"""

    __tablename__ = "moves"
    id = db.Column(db.Integer, primary_key=True)
    battle_id = db.Column(db.Integer, db.ForeignKey('battles.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_accounts.id'), nullable=False)
    round_number = db.Column(db.Integer, nullable=False, unique=False)
    time_made = db.Column(db.DateTime, nullable=False, unique=False)
