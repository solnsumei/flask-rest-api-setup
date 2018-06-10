from passlib.hash import bcrypt_sha256 as sha256
from .basemodel import BaseModel, db


class UserModel(BaseModel):
    __tablename__ = "users"

    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(15))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(8), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False)

    def __init__(self, name, password, email, phone=None,  is_admin=False):
        self.password = password
        self.name = name
        self.email = email
        self.is_admin = is_admin
        self.phone = phone
        self.status = 'active'

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_all_omit_record_with_this_email(cls, email):
        return cls.query.filter_by(cls.email != email).all()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hashed_password):
        return sha256.verify(password, hashed_password)
