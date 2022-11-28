import pandas as pd
import sql_connection
from sqlalchemy.types import Integer, Date, DECIMAL

# establish excel filepath
filepath = r'./excel/MRKTRATE - 09.21.2022.xlsx'

# import data
df = pd.read_excel(filepath, sheet_name='Treasury Rates', header=2)

# rename columns
col_names = [x.lower().replace(' ', '_') for x in df.columns.values]
df.columns = col_names

# drop na values, convert to decimal
df.dropna(inplace=True)
for col in col_names[1:]:
    df[col] = round(df[col].astype('float') / 100, 4)

# connect to sql
engine = sql_connection.conn('market_data', alchemy=True)

# import schema info for column names
schema_info = engine.execute("""
  SELECT *
  FROM information_schema.columns
  WHERE table_name = 'treasury_rates'
  ;""").fetchall()

# convert to pandas df
schema_df = pd.DataFrame(schema_info)
col_names = list(schema_df.column_name)

# update column names within df and upload
df.columns = col_names

# create data types
dtype_dict = {}
for col in col_names:
  if col != 'date':
    dtype_dict.update({col: DECIMAL})
  else:
    dtype_dict.update({col: Date})

# upload to SQL
df.to_sql('treasury_rates', con=engine, if_exists='append', index=False, dtype=dtype_dict)

engine.close()