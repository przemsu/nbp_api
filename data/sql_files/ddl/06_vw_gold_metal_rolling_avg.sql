create or replace view gold_metal_rolling_avg as 
select gdl.effective_date
     , gdl.endpoint_type as metal_name
     , round(avg(gdl.price) over (order by gdl.effective_date rows between 6 preceding and current row), 2)   as roll_avg_gold_7_days
     , round(avg(gdl.price) over (order by gdl.effective_date rows between 29 preceding and current row), 2)  as roll_avg_gold_30_days
     , round(avg(gdl.price) over (order by gdl.effective_date rows between 89 preceding and current row), 2)  as roll_avg_gold_90_days
     , round(avg(gdl.price) over (order by gdl.effective_date rows between 364 preceding and current row), 2) as roll_avg_gold_365_days
from silver_gold_rates gdl
;