CREATE TABLE IF NOT EXISTS libor_rates (
  date                DATE,
  one_mo_rate         DECIMAL(5, 4),
  two_mo_rate         DECIMAL(5, 4),
  three_mo_rate       DECIMAL(5, 4),
  four_mo_rate        DECIMAL(5, 4),
  five_mo_rate        DECIMAL(5, 4),
  six_mo_rate         DECIMAL(5, 4),
  one_yr_rate         DECIMAL(5, 4)
);
