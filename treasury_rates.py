import data_process

# establish excel filepath
filepath = r'./excel/MRKTRATE - 09.21.2022.xlsx'

def main():
  try:
    # process data
    data_process.data_processing(filepath, sheet_name='Treasury Rates', header=2, db_name='market_data', table_name='treasury_rates')
  except:
    #TODO: add logging
    print('there was an error in the process')

if __name__ == '__main__':
  main()