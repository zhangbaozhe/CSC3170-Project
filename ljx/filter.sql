USE `CommentSystem`;

SET @CourseName= concat('%','CSC','%');
-- SELECT * FROM `Courses` WHERE `CourseName`= @CourseName;
SELECT * FROM `Courses` WHERE `CourseName`LIKE @CourseName; -- fuzzy search

SET @CourseNumber= concat('___','3','%');
-- SELECT * FROM `Courses` WHERE `CourseName`= @CourseName;
SELECT * FROM `Courses` WHERE `CourseName`LIKE @CourseNumber; -- fuzzy search

-- School filter
SET @School= 'SDS';
SELECT * FROM `Courses` WHERE `School`= @School;

SET @School= 'SSE';
SELECT * FROM `Courses` WHERE `School`= @School;

SET @School= 'HSS';
SELECT * FROM `Courses` WHERE `School`= @School;

SET @School= 'SME';
SELECT * FROM `Courses` WHERE `School`= @School;

-- FinalScore filter
SET @Score= '3.3';
SELECT * FROM `Courses` WHERE `FinalScore` >= @Score;

SELECT * FROM `Courses` WHERE `FinalScore` >= (SELECT avg(`FinalScore`) FROM `Courses`);

SELECT * FROM `Courses` WHERE `FinalScore` < (SELECT avg(`FinalScore`) FROM `Courses`);





