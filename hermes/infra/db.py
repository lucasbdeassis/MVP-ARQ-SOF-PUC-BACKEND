from contextlib import contextmanager

from sqlalchemy import MetaData, create_engine

DB_URL = "sqlite:///db.sqlite3"

engine = create_engine(DB_URL, echo=False)

metadata = MetaData()


@contextmanager
def db_connection():
    connection = engine.connect()
    try:
        yield connection
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.commit()
        connection.close()


def get_connection():
    connection = engine.connect()
    return connection
