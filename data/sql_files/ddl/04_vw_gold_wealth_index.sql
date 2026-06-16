create or replace view gold_wealth_index as 
select curr.table_type
     , curr.effective_date
     , curr.currency
     , curr.code
     , curr.mid
     , gd.price
     , cast(curr.mid / gd.price as decimal(18,8)) as purchase_idx_per_currency
     , cast(1 / gd.price as decimal(18, 8))       as purchase_idx_pln
     , round(gd.price / curr.mid, 4)::DOUBLE as cost_of_one_gram_per_currency
from silver_mid_currencies_rates curr
inner join silver_gold_rates gd
on curr.effective_date = gd.effective_date
;