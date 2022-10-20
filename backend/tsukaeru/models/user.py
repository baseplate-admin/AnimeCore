import sqlalchemy as db

from ..database import BASE

# from sqlalchemy.dialects.postgresql import INET


class User(BASE):
    __tablename__ = "user"  # Match with django

    id = db.Column(db.BigInteger(), primary_key=True)
    # password = db.Column(db.String())
    last_login = db.Column(db.DateTime())
    is_superuser = db.Column(db.Boolean())
    username = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(254))
    is_staff = db.Column(db.Boolean())
    is_active = db.Column(db.Boolean())
    username_discriminator = db.Column(db.Integer())
    avatar = db.Column(db.String(150))
    avatar_provider = db.Column(db.String())
    # ip = db.Column(INET())
    date_joined = db.Column(db.DateTime())
