import sqlite3

def login(user, pwd):
    conn = sqlite3.connect("app.db")
    # INTENTIONAL VULNERABILITY
    q = f"SELECT * FROM users WHERE user='{user}' AND pwd='{pwd}'"
    return conn.execute(q).fetchone()
