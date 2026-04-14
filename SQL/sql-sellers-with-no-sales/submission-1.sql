-- Write your query below

SELECT seller_name from seller WHERE seller_id NOT IN (
SELECT seller_id FROM orders WHERE EXTRACT(YEAR FROM sale_date) = 2020) ORDER BY 1