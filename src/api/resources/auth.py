from flask_restful import Resource
from werkzeug.security import safe_str_cmp
from src.models.user import UserModel
from src.models.schemas.user import UserSchema, user_summary

user_schema = UserSchema()


class Register(Resource):
    @staticmethod
    @UserSchema.validate_fields(location=('json',))
    def post(args):

        if not safe_str_cmp(args['password'], args['password_confirmation']):
            return {
                'success': False,
                'errors': {
                    'password': ['Password and password confirmation do not match']}
            }, 409

        user = UserModel.find_by_email(args['email'])
        if user:
            return {
                'success': False,
                'error': 'Email has already been taken'
            }, 409

        is_admin = False
        if UserModel.count_all() < 1:
            is_admin = True

        phone = None

        if 'phone' in args:
            phone = args['phone']

        hashed_password = UserModel.generate_hash(args['password'])

        user = UserModel(args['name'], hashed_password, args['email'], phone, is_admin)
        user.save_to_db()

        return {
            'success': True,
            'user': user_summary.dump(user).data
        }, 201

