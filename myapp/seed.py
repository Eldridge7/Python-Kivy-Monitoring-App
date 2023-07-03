from myapp.auth.admin import is_valid_email, is_valid_password
from werkzeug.security import generate_password_hash
from myapp.db.db import Database

def seed_admin(email: str, password: str):
    if not is_valid_email(email) or not is_valid_password(password):
        raise ValueError("Invalid email or password.")
    
    hashed_password = generate_password_hash(password)
    
    query = "INSERT INTO users (email, password, role) VALUES (%s, %s, 'admin')"

    db = Database()
    db.execute(query, (email, hashed_password,))

if __name__ == "__main__":
    import getpass
    email = input("Enter the admin's email: ")
    password = getpass.getpass("Enter the admin's password: ")
    seed_admin(email, password)
    print("Admin user seeded successfully.")
