import hashlib
import re
from werkzeug.security import generate_password_hash, check_password_hash
from myapp.db.db import Database


def register_user(email, password):
    db = Database()
    if not is_valid_email(email) or not is_valid_password(password):
        return False
    # role for regular users is set by default
    query = "INSERT INTO users (email, password) VALUES (%s, %s)"
    hashed_password = generate_password_hash(password)
    db.execute(query, (email, hashed_password))
    return True  # since an error will be raised on failure, getting to this line means it was successful.

def validate_user(email, password):
    db = Database()
    cursor = db.connection.cursor()
    cursor.execute("SELECT password FROM users WHERE email=%s AND role='user'", (email,))
    user = cursor.fetchone()
    if user is not None:
        return check_password_hash(user[0], password)
    return False


def get_user_id(email): 
    db = Database()
    cursor = db.connection.cursor()
    cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    if user is not None:
        return user[0]
    return -1
def is_valid_email(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(email_regex, email) is not None

def is_valid_password(password):
    return len(password) >= 8
