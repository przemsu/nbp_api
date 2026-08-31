create or replace view gold_currency_spread as
select bs.effective_date
     , bs.trading_date
     , bs.currency
     , bs.code
     , round(bs.ask - bs.bid, 4)as daily_spread
     , round(((bs.ask - bs.bid)/ bs.final_rate) * 100, 4) as pct_daily_spread
     , round(avg(bs.ask - bs.bid) over (partition by bs.code order by bs.effective_date rows between 6 preceding and current row), 4)   as roll_avg_currency_spread_7_days 
     , round(avg(bs.ask - bs.bid) over (partition by bs.code order by bs.effective_date rows between 29 preceding and current row), 4)  as roll_avg_currency_spread_30_days 
     , round(avg(bs.ask - bs.bid) over (partition by bs.code order by bs.effective_date rows between 89 preceding and current row), 4)  as roll_avg_currency_spread_90_days 
     , round(avg(bs.ask - bs.bid) over (partition by bs.code order by bs.effective_date rows between 364 preceding and current row), 4) as roll_avg_currency_spread_365_days 
from silver_buy_sell_currencies_rates bs
;