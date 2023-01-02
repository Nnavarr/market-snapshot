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
  print(df.head())

  print('starting logic for additional data cleaning')
  # rename columns
  if 'cad' in table_name:
    df = df.iloc[:, 3:5]
    col_names = ['date', 'rate']
    df.columns = col_names

  elif 'prime' in table_name:
    df = df.iloc[:, 0:2]
    col_names = ['date', 'rate']
    df.columns = col_names
  else:
    col_names = [x.lower().replace(' ', '_') for x in df.columns.values]
    df.columns = col_names

  print('made it through the initial sequence...')
  # drop na & text values, convert to decimal
  df.dropna(inplace=True)
  df = df[df.iloc[:, 1].apply(lambda x: isinstance(x, float))]
  for col in col_names[1:]:
    # generate decimal value, exclude volume columns
    if 'vol' not in col:
      df[col] = round(df[col].astype('float') / 100, 4)

  print('starting to import table schema')
  # import schema from sql table
  engine = sql_connection.conn(db_name, alchemy=True)
  print('engine created successfully...')

  # import schema info for column names
  schema_info = engine.execute("""
    SELECT *
    FROM information_schema.columns
    WHERE table_name = '{}'
  ;""".format(table_name)).fetchall()
  print('schema fetched successfully...')

  # convert to pandas df
  schema_df = pd.DataFrame(schema_info)
  print(schema_df)
  col_names = list(schema_df.column_name)
  print(col_names)

  # update column names within df and upload
  df.columns = col_names

  # create data types
  dtype_dict = {}
  for col in col_names:
    if col != 'date':
      dtype_dict.update({col: DECIMAL})
    else:
      dtype_dict.update({col: Date})
  print('data processed successfully...')

  # upload to SQL
  df.to_sql(table_name, con=engine, if_exists='replace', index=False)
  print('table uploaded to SQL successfully!')

  # close connection
  engine.close()
