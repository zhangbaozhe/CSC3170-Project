SELECT `UserID`
FROM `Comments`
WHERE `CourseID`=%s;

SELECT  
`CommentID`, u.`UserID`, `UserName`, `CourseID`, 
`Semester`, `Year`, `Instructor`, 
`Score`, `Content`, `LikeNum`, `DislikeNum`
FROM `Comments` c, `Users` u
WHERE `CourseID`=%s and u.`UserID` = c.UserID;

SELECT * 
FROM `CommentLikeStatus`
WHERE `CommentID`=%s;


