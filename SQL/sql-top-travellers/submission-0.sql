-- Write your query below

SELECT
    u.name,
    sum(coalesce(r.distance, 0)) AS travelled_distance
FROM users u LEFT JOIN rides r ON u.id = r.user_id
GROUP BY 1 ORDER BY 2 DESC, 1 ASC
