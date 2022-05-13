SELECT *
FROM `courses` as c1,
(SELECT COUNT(*) as count, ROUND(AVG(comments.score),1) as a, courses.courseid
FROM `courses`,`comments`
where courses.courseid = comments.courseid
group by courses.courseid) as c
where c1.courseid = c.courseid;

SELECT *
FROM `courses` as c1,
(SELECT COUNT(*) as count, ROUND(AVG(comments.score),1) as a, courses.courseid
FROM `courses`,`comments`
where courses.courseid = comments.courseid
group by courses.courseid) as c
where c1.courseid = c.courseid
and c1.coursename like '{Subject}%'
and (c1.coursename like '%{Content}%'
or c1.school like '%{Content}%'
            
SELECT *
FROM `courses` as c1,
(SELECT COUNT(*) as count, ROUND(AVG(comments.score),1) as a, courses.courseid
FROM `courses`,`comments`
where courses.courseid = comments.courseid
group by courses.courseid) as c
where c1.courseid = c.courseid
and c1.school = '{Department}'
and c1.coursename like '{Subject}%'
and (c1.coursename like '%{Content}%'
or c1.school like '%{Content}%'
