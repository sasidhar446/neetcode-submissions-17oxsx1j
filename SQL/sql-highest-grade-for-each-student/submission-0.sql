-- Write your query below

SELECT 
    er.student_id
    ,min(er.exam_id) AS exam_id
    ,max(er.score) AS score
FROM exam_results er JOIN
(SELECT
    student_id, max(score) AS score
FROM exam_results
GROUP BY 1) sm
ON er.student_id = sm.student_id AND er.score = sm.score
GROUP BY 1
