from functools import wraps

from flask import g, request

from hermes.application.factories import InjectorFactory


def requires_auth(admin_only=False):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            with InjectorFactory() as factory:
                token = request.headers.get("Authorization")
                if not token:
                    return {"erro": "missing authorization header"}, 401
                user = factory.auth_service().verify_token(token)
                if not user:
                    return {"erro": "invalid token"}, 401
                user = factory.user_service().get_user_by_id(user)
                if admin_only and not user.is_admin:
                    return {"erro": "user role not authorized"}, 401
                g.user = user
                return f(*args, **kwargs)

        return decorated

    return decorator
