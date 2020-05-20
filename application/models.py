from . import db

# DEFINE YOUR MODELS HERE

"""
EXAMPLE 

class User(db.Model):
    __tablename__ = 'test_table_flask'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    created = db.Column(db.DateTime, unique=True, nullable=False)
    bio = db.Column(db.Text, unique=True, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'User {self.username}'
"""