-- Life span of metal bands with galm rock style

SELECT band_name,
CASE
    WHEN split IS NULL THEN 2022 - formed
    ELSE split - formed
END AS lifespan
from metal_bands
where style LIKE '%Glam rock%'
Order by lifespan DESC;
