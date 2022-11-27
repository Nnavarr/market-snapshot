import pandas as pd

# establish excel filepath
filepath = r'./excel/MRKTRATE - 09.21.2022.xlsx'

# import data
df = pd.read_excel(filepath, sheet_name='Treasury Rates', header=2)

df.head()
df.info()

# rename columns
col_names = [x.lower().replace(' ', '_') for x in df.columns.values]