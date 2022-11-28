import pandas as pd
import sqlalchemy

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
    df[col] = df[col].astype('float') / 100

# upload to sql
conn = sql_connection.conn('market_data')
cursor = conn.cursor()
cursor.close()
conn.close()

# upload to sql
df.to_sql('treasury_rates', con=conn, if_exists='replace', index=False)