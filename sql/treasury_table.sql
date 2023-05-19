CREATE TABLE IF NOT EXISTS treasury_rates (
  date                DATE,
  two_yr_rate         DECIMAL(5, 4),
  three_yr_rate       DECIMAL(5, 4),
  five_yr_rate        DECIMAL(5, 4),
  seven_yr_rate       DECIMAL(5, 4),
  ten_yr_rate         DECIMAL(5, 4),
  twenty_yr_rate      DECIMAL(5, 4),
  thirty_yr_rate      DECIMAL(5, 4)
);
