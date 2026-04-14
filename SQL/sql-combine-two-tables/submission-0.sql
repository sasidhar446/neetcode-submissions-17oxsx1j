-- Write your query below

SELECT
 p.first_name
,p.last_name
,a.city
,a.state
FROM person p LEFT join address a ON p.person_id = a.person_id