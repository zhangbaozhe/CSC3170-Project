SELECT *
FROM `courses` as c1,
(SELECT 
    COUNT(*) as count, 
    ROUND(AVG(comments.score),1) as a,
    courses.courseid
    FROM `courses`,`comments`
    where courses.courseid = comments.courseid
    group by courses.courseid) 
as c
where c1.courseid = c.courseid;
