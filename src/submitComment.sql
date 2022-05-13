INSERT INTO `Comments` (
`UserID`, `Year`, `Semester`, 
`Instructor`, `Score`, 
`Content`, `LikeNum`, `DislikeNum`, 
`CourseID`) 
VALUES (
%s, %s, %s, %s, %s, 
%s, %s, %s, %s)
