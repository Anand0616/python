import database
from sqlalchemy import create_engine

def connect():
    engine = create_engine("mysql://" + database.user + ":" +
                           database.password + "@" + database.server, echo=True)
    return engine


def create(db):
    engine = connect()
    engine.execute("CREATE DATABASE IF NOT EXISTS " + db) 


def use(db):
    engine = connect()
    engine.execute("USE " + db) 
    return engine