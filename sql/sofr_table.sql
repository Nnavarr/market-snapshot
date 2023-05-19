CREATE TABLE IF NOT EXISTS sofr (
  date                DATE,
  rate                DECIMAL(5, 4),
  first_pctl          DECIMAL(5, 4),
  twenty_fifth_pctl   DECIMAL(5, 4),
  seventy_fifth_pctl  DECIMAL(5, 4),
  ninety_ninth_pctl   DECIMAL(5, 4),
  volumne_us_billions INTEGER
);

