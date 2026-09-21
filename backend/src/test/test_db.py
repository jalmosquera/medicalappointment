from core.db.db import engine, get_session
from sqlmodel import text


def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1


def test_database_session():
    session_generator = get_session()
    session = next(session_generator)

    try:
        result = session.exec(text("SELECT 1"))
        assert result.scalar_one() == 1
    finally:
        session_generator.close()
