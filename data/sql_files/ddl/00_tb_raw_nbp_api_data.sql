create or replace table raw_nbp_api_data (
    endpoint_type       varchar,
    extraction_date     date,
    raw_content         json,
    loaded_at           timestamp default current_timestamp,
    unique(endpoint_type, extraction_date)
)
;