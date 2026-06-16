create or replace view silver_gold_rates as 
select 
      endpoint_type                       as endpoint_type,
      extraction_date                     as extraction_date,
      (raw_content->>'$.data')::DATE      as effective_date,
      (raw_content->>'$.cena')::DOUBLE    as price 
from raw_nbp_api_data 
where endpoint_type = 'gold'
;