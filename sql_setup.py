import sql_connection
import os

# sql files
sql_files = os.listdir('./sql')

# database creation
with open(f'./sql/market_db.sql') as f:
  db_creation = f.read()

  # create connection to PostgreSQL
  conn = sql_connection.conn('postgres')
  conn.autocommit = True
  cursor = conn.cursor()
  cursor.execute(db_creation)

  # close connections
  cursor.close()
  conn.close()
  
# establish connection for table creation
conn = sql_connection.conn('market_data')
cursor = conn.cursor()

# table creation (skip db creation file)
for file in sql_files:
  if 'db' not in file:
    with open(f'./sql/{file}') as f:
      print(f'{file} started...')
      sql_file = f.read()
      cursor.execute(sql_file)
      print(f'{file} complete.')
      
# commit and close connections
conn.commit()
cursor.close()
conn.close()