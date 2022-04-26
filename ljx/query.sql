USE `CommentSystem`;


SET @CourseID = `1`;
SELECT * FROM comments WHERE `CourseID` = @CourseID;

