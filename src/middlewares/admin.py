from functools import wraps
from flask_jwt import current_identity


def admin_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_identity.is_admin:
                return {"error": "Unauthorized user"}, 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator
