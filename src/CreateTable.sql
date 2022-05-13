
-- Users
CREATE TABLE IF NOT EXISTS `Users` (
    `UserID` INTEGER PRIMARY KEY NOT NULL, 
    `Username` VARCHAR(25) NOT NULL, -- set as distinct user name
    `Password` VARCHAR(30) NOT NULL  -- TODO: can be set as infinite long? 
);

-- Give -> change to UsersGiveComments
CREATE TABLE IF NOT EXISTS `UsersGiveComments` (
    `UserID` INT(8) NOT NULL, 
    `CommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`UserID`, `CommentID`)
);



-- Evaluate --> change to CommentsEvaluateCourses
CREATE TABLE IF NOT EXISTS `CommentsEvaluateCourses` (
    `CourseID` VARCHAR(10) NOT NULL, 
    `CommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`CourseID`, `CommentID`)
);

-- Courses
CREATE TABLE IF NOT EXISTS `Courses` (
    `CourseID` INTEGER PRIMARY KEY NOT NULL, 
    `CourseName` VARCHAR(30) NOT NULL, 
    `School` VARCHAR(30) NOT NULL, -- department changed to school
    `Credits` INT(1) NOT NULL, 
    `IsValid` BOOLEAN NOT NULL, -- TODO: future feature: 1 admin added, 0 user added
    `FinalScore` DECIMAL(2,1) 
);

-- Comments
CREATE TABLE IF NOT EXISTS `Comments` (
    `CommentID` INTEGER PRIMARY KEY NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    `CourseID` INTEGER  NOT NULL, 
    `Semester` INT(1), -- TODO: finite insertion
    `Year` INT(4),  
    `Instructor` VARCHAR(20), -- null?
    `Score` DECIMAL(2,1) NOT NULL, 
    `Content` VARCHAR(140), 
    `LikeNum` INT(5) NOT NULL, 
    `DislikeNum` INT(5) NOT NULL, 
    FOREIGN KEY (`CourseID`) REFERENCES `Courses` (`CourseID`)
);

-- Appraise
CREATE TABLE IF NOT EXISTS `CommentLikeStatusAppraiseComments` (
    `CommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    PRIMARY KEY (`CommentID`, `UserID`)
);

-- CommentLikeStatus
CREATE TABLE IF NOT EXISTS `CommentLikeStatus` (
    `CommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    `Status` INT(1) NOT NULL,  -- TODO: three states, like, dislike, neutral
    PRIMARY KEY (`CommentID`, `UserID`)
);

-- Set TODO: maybe redaundant 
CREATE TABLE IF NOT EXISTS `UsersSetCommentLikeStatus` (
    `CommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    PRIMARY KEY (`CommentID`, `UserID`)
);

CREATE TABLE IF NOT EXISTS `MultiComments` (
    `MultiCommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    `Content` VARCHAR(140), 
    `ParentCommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`MultiCommentID`)
);

-- Reply
CREATE TABLE IF NOT EXISTS `MultiCommentsReplyComments` (
    `CommentID` INT(8) NOT NULL, 
    `MultiCommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`CommentID`, `MultiCommentID`)
);

