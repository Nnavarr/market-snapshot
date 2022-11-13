import psycopg2

# establish connection to postgresql
conn = psycopg2.connect(
  host='localhost',
  database='market_data',
  user='postgres',
  password=''
)