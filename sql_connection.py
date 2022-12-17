import psycopg2
import os
from dotenv import load_dotenv

# establish connection to postgresql
def postgresql_con(database):
  conn = psycopg2.connect(
    host='localhost',
    database=database,
    user=os.getenv('PGUSER'),
    password=os.getenv('PGPASSWORD')
  )
  return conn

# example connection
# conn = postgresql_con()
# cursor = conn.cursor()
# cursor.execute('SELECT version()')
# cursor.fetchone()
# cursor.close()