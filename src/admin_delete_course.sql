DELETE FROM `Comments`
WHERE `CourseID` = %d;

DELETE FROM `CommentsEvaluateCourses`
WHERE `CourseID` = %d;

DELETE FROM `Courses`
WHERE `CourseID` = %d;