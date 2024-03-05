from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base_DB_Model = declarative_base()
engine = create_engine(
    "postgresql://{YOUR_DATABASE_USER}:{YOUR_DATABASE_PASSWORD}@localhost/{YOUR_DATABASE_NAME}",
    echo=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_session(*args, **kwargs):
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
