import pandas as pd
import sql_connection

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
engine = sql_connection.conn('market_data', alchemy=True)
df.to_sql('treasury_rates', con=engine, if_exists='replace', index=False)

# close connection
engine.close()