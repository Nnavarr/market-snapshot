import sql_connection
import os

# sql files
sql_files = os.listdir('./sql')

# create connection to PostgreSQL
conn = sql_connection.conn

# iterate through db/table creation files
for file in sql_files:
  print(file)
  with open(f'./sql/{file}') as f:
    sql_file = f.read()
    print(sql_file)

