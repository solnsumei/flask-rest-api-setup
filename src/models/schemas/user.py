from marshmallow import fields, validate, post_load
from src.utils.validators import name_field, validate_len
from .base import BaseSchema


class UserSchema(BaseSchema):
    name = name_field
    email = fields.Email(required=True)
    phone = fields.Int(
        validate=[validate.Length(min=11, max=15), lambda p: validate_len(p, 11)]
    )
    password = fields.Str(load_only=True, required=True, validate=lambda p: validate_len(p, 8))
    password_confirmation = fields.Str(required=True, load_only=True)

    @post_load()
    def user_details_strip(self, data):
        data['email'] = data['email'].lower().strip()


user_summary = UserSchema(exclude=('updated_at',))
