import os

DB_URL = os.getenv("DB_URL", "sqlite:///./db.sqlite3")
SECRET = os.getenv("SECRET", "secret")
