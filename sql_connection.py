import psycopg2
import sqlalchemy
from dotenv import load_dotenv
import os

# load variables
load_dotenv()
username = os.getenv('PGUSER')
password = os.getenv('PGPASSWORD')

# establish connection to postgresql
def conn(database, alchemy=False):
  if alchemy is False:
    conn = psycopg2.connect(
      host='localhost',
      # port=5432,
      database=database,
      user=username,
      password=password
    )
    return conn
  
  # create sqlalchemy connection (pandas upload)
  engine = sqlalchemy.create_engine(f'postgresql://postgres:{username}@localhost/{database}')
  return engine.connect()