from functools import wraps
from flask_jwt_extended import current_user


def admin_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_admin:
                return {"error": "Unauthorized user"}, 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator
