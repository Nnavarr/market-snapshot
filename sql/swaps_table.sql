CREATE TABLE IF NOT EXISTS swap_rates (
  date                    DATE,
  one_yr_rate             DECIMAL(5, 4),
  two_yr_rate             DECIMAL(5, 4),
  three_yr_rate           DECIMAL(5, 4),
  five_yr_rate            DECIMAL(5, 4),
  seven_yr_rate           DECIMAL(5, 4),
  ten_yr_rate             DECIMAL(5, 4),
  thirty_yr_rate          DECIMAL(5, 4)
);