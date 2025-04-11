from dotenv import load_dotenv
from sqlalchemy import URL
import os
import logging

logger = logging.getLogger(__name__)
class Config:
    def get_env(self):
        try:
            current_env = os.environ['ENVIROMENT']
            return current_env
        except:
            return None

    def get_db_config(self):
        if not self.get_env():
            load_dotenv()
            url_object = URL.create(
                drivername='postgresql+psycopg2',
                username= os.environ['DEV_DB_USER_NAME'],
                password= os.environ['DEV_DB_PASSWORD'],
                host=os.environ['DEV_DB_HOST'],
                port=5432,
                database=os.environ['DEV_DB_DATABASE_NAME'],
            )
            return url_object
        else:
            url_object = URL.create(
                drivername='postgresql+psycopg2',
                username= os.environ['DEV_DB_USER_NAME'],
                password= os.environ['DEV_DB_PASSWORD'],
                host=os.environ['DEV_DB_HOST'],
                port=5432,
                database=os.environ['DEV_DB_DATABASE_NAME'],
            )
            return url_object
