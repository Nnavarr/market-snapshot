import pandas as pd
import sql_connection
from sqlalchemy.types import Integer, Date, DECIMAL

def data_processing(filepath: str, sheet_name: str, header: int, db_name: str, table_name: str):
  """
  Author: Noe Navarro
  Date: 2022-11-29
  Objective:
    This function was created in order to process the individual rate files.
  """
  df = pd.read_excel(filepath, sheet_name=sheet_name, header=header)

  # rename columns
  col_names = [x.lower().replace(' ', '_') for x in df.columns.values]
  df.columns = col_names

  # drop na values, convert to decimal
  df.dropna(inplace=True)
  for col in col_names[1:]:
    df[col] = round(df[col].astype('float') / 100, 4)

  # import schema from sql table
  engine = sql_connection.conn(db_name, alchemy=True)

  # import schema info for column names
  schema_info = engine.execute("""
    SELECT *
    FROM information_schema.columns
    WHERE table_name = '{}'
  ;""".format(table_name)).fetchall()

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
  df.to_sql(table_name, con=engine, if_exists='replace', index=False)

  # close connection
  engine.close()
