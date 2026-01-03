
Insecure Authentication Application


import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

conn.commit()


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("Login successful")
    else:
        print("Login failed")


if __name__ == "__main__":
    login()
