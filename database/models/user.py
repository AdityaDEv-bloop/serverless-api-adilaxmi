from sqlalchemy import  create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from config.db_config import Config

db_config = Config()
url_object = db_config.get_db_config()
engine = create_engine(url_object)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    phone = Column(String,nullable=False)
    password = Column(String,nullable=False)

# create the database tables
Base.metadata.create_all(engine)