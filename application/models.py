from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """Data model for user accounts"""

    __tablename__ = "user_acounts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=False, unique=False, nullable=False)
    username = db.Column(db.String(50), index=True, unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(50), index=False, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def set_password(self, password):
        """Create password hash"""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check password hash"""
        return check_password_hash(self.password, password)

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Username {}>'.format(self.username)
