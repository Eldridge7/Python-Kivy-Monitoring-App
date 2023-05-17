import hashlib
import re
from werkzeug.security import generate_password_hash, check_password_hash
from myapp.db import create_connection


def register_user(email, password):
    connection = create_connection("localhost", "root", "079Geo@712", "app_db")
    if not is_valid_email(email) or not is_valid_password(password):
        return False
    cursor = connection.cursor()
    query = "INSERT INTO users (email, password) VALUES (%s, %s)"
    hashed_password = generate_password_hash(password)
    cursor.execute(query, (email, hashed_password))
    connection.commit()
    return cursor.rowcount == 1

def validate_user(email, password):
    connection = create_connection("localhost", "root", "079Geo@712", "app_db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT password FROM users WHERE email='{email}'")
    user = cursor.fetchone()
    if user is not None:
        return check_password_hash(user[0], password)
    return False

def is_valid_email(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(email_regex, email) is not None

def is_valid_password(password):
    return len(password) >= 8
