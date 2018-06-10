from marshmallow import fields, validate, ValidationError


def validate_len(input_field, length):
    if len(input_field.strip()) < length:
        raise ValidationError(
            'Field must not be less than {} characters long'.format(length)
        )


name_field = fields.String(
        required=True,
        validate=lambda p: validate_len(p, 3),
        location='json',
        error_messages={'required': 'This field is required'}
    )

id_field = fields.Int(
    required=True,
    validate=lambda x: x > 0,
    location='query',
    error='Field must be greater than 0'
)

status_field = fields.String(
        required=True,
        validate=validate.OneOf(['enabled', 'disabled']),
        location='json'
    )
