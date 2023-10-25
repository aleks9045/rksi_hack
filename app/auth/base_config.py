from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from app.config import SECRET_JWT

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

SECRET = SECRET_JWT


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
