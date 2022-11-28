import psycopg2
import os
import sqlalchemy

# read password
with open('./env_var.txt') as f:
  pg_password = f.readlines()

# establish connection to postgresql
def conn(database, alchemy=False):
  if alchemy is False:
    conn = psycopg2.connect(
      host='localhost',
      database=database,
      user='postgres',
      password=pg_password[0]
    )
    return conn
  
  # create sqlalchemy connection (pandas upload)
  engine = sqlalchemy.create_engine(f'postgresql://postgres:{pg_password[0]}@localhost/{database}')
  return engine.connect()
