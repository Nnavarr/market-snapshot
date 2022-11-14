import psycopg2
import os

# read password
with open('./env_var.txt') as f:
  pg_password = f.readlines()

# establish connection to postgresql
conn = psycopg2.connect(
  host='localhost',
  database='postgres',
  user='postgres',
  password=pg_password[0]
)
