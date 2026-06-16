INSERT INTO raw_nbp_api_data (
    endpoint_type,
    extraction_date,
    raw_content
    )
VALUES (
    ?, ?, ?
    ) 
ON CONFLICT DO NOTHING
;