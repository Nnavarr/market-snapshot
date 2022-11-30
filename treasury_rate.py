import pandas as pd
import sql_connection
from sqlalchemy.types import Integer, Date, DECIMAL
import data_process

# establish excel filepath
filepath = r'./excel/MRKTRATE - 09.21.2022.xlsx'

try:
  # process data
  data_process.data_processing(filepath, sheet_name='Treasury Rates', header=2, db_name='market_data', table_name='treasury_rates')
except:
  print('there was an error in the process')