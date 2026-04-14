-- Write your query below

-- SELECT 
--     er.student_id
--     ,min(er.exam_id) AS exam_id
--     ,max(er.score) AS score
-- FROM exam_results er JOIN
-- (SELECT
--     student_id, max(score) AS score
-- FROM exam_results
-- GROUP BY 1) sm
-- ON er.student_id = sm.student_id AND er.score = sm.score
-- GROUP BY 1


-- SELECT DISTINCT ON (student_id)
--     student_id,
--     exam_id,
--     score
-- FROM exam_results
-- ORDER BY student_id, score DESC, exam_id ASC;

SELECT student_id, exam_id, score FROM (
SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY score DESC, exam_id ASC) AS rn
FROM exam_results) WHERE rn = 1

