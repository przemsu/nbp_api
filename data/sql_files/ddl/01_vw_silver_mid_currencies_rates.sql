create or replace view silver_mid_currencies_rates AS 
with rates_unnested AS (
select 
      endpoint_type                                  as endpoint_type,
      extraction_date                                as extraction_date,
      raw_content->>'$.table'                        as table_type,
      raw_content->>'$.no'                           as no,
      raw_content->>'$.effectiveDate'                as effective_date,
      raw_content->>'$.tradingDate'                  as trading_date,
      unnest(cast(raw_content->'$.rates' as JSON[])) as rate_obj
from raw_nbp_api_data
where endpoint_type != 'gold'
and (raw_content->>'$.table')::VARCHAR in ('A', 'B')
)
select 
      endpoint_type                                  as endpoint_type,
      extraction_date                                as extraction_date,
      table_type                                     as table_type,
      no                                             as no,
      effective_date                                 as effective_date,
      trading_date                                   as trading_date,
      rate_obj->>'$.currency'                        as currency,
      rate_obj->>'$.code'                            as code,
      round((rate_obj->>'$.mid')::DOUBLE, 5)         as mid
from rates_unnested
;