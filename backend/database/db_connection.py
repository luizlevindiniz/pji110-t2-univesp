from contextlib import contextmanager
from typing import Generator

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# criar conexao com o postgres usando sql alchemy e psycog2
# https://github.com/jod35/Build-a-fastapi-and-postgreSQL-API-with-SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False)
# bind=db_connection.engine
Base_DB_Model = declarative_base()


@contextmanager
def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise e
    finally:
        session.close()
