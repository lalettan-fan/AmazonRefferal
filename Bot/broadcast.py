from sqlalchemy import Column, String, Integer
import os
from Bot.config import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

if DB_URI.startswith('postgres'):
    DB_URI = DB_URI.replace('postgres', 'postgresql', 1)


def start() -> scoped_session:
    engine = create_engine(DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print("DB_URI is not configured. Features depending on the database might have issues.")
    print(str(e))


class userbase(BASE):
    __tablename__ = "UserDB"
    chat_id = Column(String(14), primary_key=True)
    refferal = Column(Integer)
    refferedby = Column(Integer)

    def __init__(self, chat_id, refferal, refferedby):
        self.chat_id = chat_id
        self.refferal = refferal
        self.refferedby = refferedby


userbase.__table__.create(checkfirst=True)


def add_to_userbase(chat_id: int, user_id):
    __user = userbase(str(chat_id), 0, int(user_id))
    SESSION.add(__user)
    SESSION.commit()


def del_from_userbase(chat_id: int):
    user = SESSION.query(userbase).get(str(chat_id))
    SESSION.delete(user)
    SESSION.commit()

def get_from_userbase(chat_id: int):
    user = SESSION.query(userbase).get(str(chat_id))
    return user


def full_userbase():
    users = SESSION.query(userbase).all()
    SESSION.close()
    return users


def present_in_userbase(chat_id):
    try:
        return SESSION.query(userbase).filter(
            userbase.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_count(chat_id):
    user = SESSION.query(userbase).filter(userbase.chat_id == str(chat_id)).one()
    return user.refferal


def edit_count(chat_id, refferal):
    SESSION.query(userbase).filter(userbase.chat_id == str(chat_id)).update({userbase.refferal: refferal})
    SESSION.commit()
