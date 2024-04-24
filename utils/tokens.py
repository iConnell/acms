import jwt
from decouple import config
from datetime import datetime, timedelta


# Assuming email is the ID of the user for whom you want to generate the token
def generate_token(email):
    expiration_time = datetime.now() + timedelta(minutes=10)

    payload = {'email': email, 'exp': expiration_time}

    token = jwt.encode(payload, config('JWT_SECRET'), algorithm='HS256')
    return token


def decode_token(token):
    try:
        payload = jwt.decode(token, config('JWT_SECRET'), algorithms=['HS256'])
        email = payload['email']
        return email
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        # Token expired
        return None
