from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base_DB_Model = declarative_base()
engine = create_engine(
    "postgresql://admin:YrQmziLDIQZjwg8HW2mejfPk7cXmTN8u@dpg-coa0ak21hbls73fgvva0-a.ohio-postgres.render.com/fmcdb",
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
