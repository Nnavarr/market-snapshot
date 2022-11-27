import psycopg2
import os

# read password
with open('./env_var.txt') as f:
  pg_password = f.readlines()

# establish connection to postgresql
def conn(database):
  conn = psycopg2.connect(
    host='localhost',
    database=database,
    user='postgres',
    password=pg_password[0]
  )
  return conn
