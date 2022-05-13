INSERT INTO `Courses` 
(
    `CourseName`, `CourseFullName`, 
    `School`, `Credits`, 
    `IsValid`, `FinalScore`
) 
VALUES 
(%s, %s, %s, %d, 1, 0.0);

