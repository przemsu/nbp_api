create or replace view gold_currency_rolling_avg as 
select curr.effective_date
     , curr.currency as currency_name
     , curr.code as currency_rate_iso_3
     , curr.mid as average_rate
     , round(avg(curr.mid) over (partition by curr.code order by effective_date rows between 6 preceding and current row), 4)   as roll_avg_curr_7_days
     , round(avg(curr.mid) over (partition by curr.code order by effective_date rows between 29 preceding and current row), 4)  as roll_avg_curr_30_days
     , round(avg(curr.mid) over (partition by curr.code order by effective_date rows between 89 preceding and current row), 4)  as roll_avg_curr_90_days
     , round(avg(curr.mid) over (partition by curr.code order by effective_date rows between 364 preceding and current row), 4) as roll_avg_curr_365_days
from silver_mid_currencies_rates curr
;