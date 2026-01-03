Secure Authentication Application

import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT UNIQUE,
    password_hash TEXT
)
""")

conn.commit()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password_hash=?",
        (username, hashed_password)
    )

    result = cursor.fetchone()

    if result:
        print("Login successful")
    else:
        print("Invalid credentials")


if __name__ == "__main__":
    login()
