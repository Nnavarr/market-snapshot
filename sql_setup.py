from sql_connection import postgresql_con
import os
import psycopg2

# sql files
sql_files = os.listdir('./sql')

# make db creation the first file
sql_files.remove('market_db.sql')

# create connection to PostgreSQL & establish table
conn = postgresql_con('postgres')
conn.autocommit = True

# create cursor object
cursor = conn.cursor()
with open(f'./sql/market_db.sql') as f:
  sql_file = f.read()
  cursor.execute(sql_file)
  cursor.close()
  conn.close()

# establish new cursor with newly created database
conn = postgresql_con('market_data')
conn.autocommit = True
cursor = conn.cursor()

# iterate through db/table creation files
for file in sql_files:
  with open(f'./sql/{file}') as f:
    print(f'starting {file}')
    sql_file = f.read()
    cursor.execute(sql_file)
    print(f'ending {file}')

# close connection
cursor.close()
conn.close()