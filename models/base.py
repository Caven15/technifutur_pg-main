from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase

class Base(MappedAsDataclass, DeclarativeBase):
    pass

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from contextlib import contextmanager
import os

load_dotenv()

url = os.getenv('DB_URL')
engine = create_engine(url=url, echo=True)

session_local = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False # attention avec les data class !!!
)

def init_db(delete=False):
    if delete:
        Base.metadata.drop_all(bind=engine)
        print("[INFOS] : Table supprimée !!")
    Base.metadata.create_all(bind=engine)
    print("[INFOS] : Table Créee !!")

@contextmanager
def get_db_session():
    """à gérer les ession proprement"""
    session = session_local()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()