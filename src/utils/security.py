from src.models.user import UserModel
from main import jwt


def authenticate(email, password):
    user = UserModel.find_by_email(email)
    if user and UserModel.verify_hash(password, user.password):
        return user


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def identity(_jwt_header, jwt_data):
    user_id = jwt_data['sub']
    return UserModel.find_by_id(user_id)
