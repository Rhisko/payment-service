import sqlite3

def setup_db():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'secret123')")
    cur.execute("INSERT INTO users (username, password) VALUES ('user1', 'pass1')")

    conn.commit()
    conn.close()


def vulnerable_login(username, password):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()

    # INTENTIONALLY VULNERABLE
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing:", query)

    cur.execute(query)
    result = cur.fetchone()

    conn.close()
    return result is not None


if __name__ == "__main__":
    setup_db()

    print("Normal login:", vulnerable_login("admin", "secret123"))
    print("Wrong password:", vulnerable_login("admin", "wrong"))

    # Example lab payload
    injected_password = "' OR '1'='1"
    print("Injected login:", vulnerable_login("admin", injected_password))