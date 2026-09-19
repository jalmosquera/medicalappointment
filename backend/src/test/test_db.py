from sqlmodel import text

from core.db.db import get_session


def test_database_session():
    session_generator = get_session()
    session = next(session_generator)

    try:
        result = session.exec(text("SELECT 1"))
        assert result.scalar_one() == 1
    finally:
        session_generator.close()
