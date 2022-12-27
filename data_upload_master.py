import cad_rates
import cme_sofr
import prime_rates
import swap_rates
import treasury_rates

# main function
def main():
  """
  Call all data upload functions 
  """
  print('starting cad...')
  cad_rates.main()
  print('starting cme_sofr...')
  cme_sofr.main()
  print('starting prime rates...')
  prime_rates.main()
  print('starting swap rates...')
  swap_rates.main()
  print('starting treasury rates...')
  treasury_rates.main()

if __name__ == '__main__':
  main()