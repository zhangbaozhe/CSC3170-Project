DROP SCHEMA IF EXISTS `CommentSystem`;
CREATE SCHEMA IF NOT EXISTS `CommentSystem` DEFAULT CHARACTER SET utf8;
USE `CommentSystem`;

-- Users
CREATE TABLE IF NOT EXISTS `Users` (
    `UserID` INT(8) NOT NULL, 
    `Username` VARCHAR(25) DISTINCT NOT NULL, -- set as distinct user name
    `Password` VARCHAR(30) NOT NULL,  -- TODO: can be set as infinite long? 
    PRIMARY KEY (`UserID`)
)ENGINE=InnoDB;

-- Give
CREATE TABLE IF NOT EXISTS `Give` (
    `UserID` INT(8) NOT NULL, 
    `CommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`UserID`, `CommentID`)
)ENGINE=InnoDB;

-- Comments
CREATE TABLE IF NOT EXISTS `Comments` (
    `CommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    `CourseID` VARCHAR(10) NOT NULL, 
    `Semester` INT(1), -- TODO: finite insertion
    `Year` INT(4),  
    `Instructor` VARCHAR(20), -- null?
    `Score` DECIMAL(2,1) NOT NULL, 
    `Content` VARCHAR(140), 
    `LikeNum` INT(5) NOT NULL, 
    `DislikeNum` INT(5) NOT NULL, 
    `Credits` INT(1) NOT NULL, -- FIXME: credit in course table
    PRIMARY KEY (`CommentID`), 
    FOREIGN KEY (`CourseID`) REFERENCES `Courses` (`CourseID`)
    -- TODO: UserID foreign key
)ENGINE=InnoDB;

-- Evaluate
CREATE TABLE IF NOT EXISTS `Evaluate` (
    `CourseID` VARCHAR(10) NOT NULL, 
    `CommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`CourseID`, `CommentID`)
)ENGINE=InnoDB;

-- Courses
CREATE TABLE IF NOT EXISTS `Courses` (
    `CourseID` VARCHAR(10) NOT NULL, 
    `CourseName` VARCHAR(30) NOT NULL, 
    `School` VARCHAR(30) NOT NULL, -- department changed to school
    `IsValid` BOOLEAN NOT NULL, -- TODO: future feature: 1 admin added, 0 user added
    `FinalScore` DECIMAL(2,1), 
    PRIMARY KEY (`CourseID`)
)ENGINE=InnoDB;

-- Appraise
CREATE TABLE IF NOT EXISTS `Appraise` (
    `CommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    PRIMARY KEY (`CommentID`, `UserID`)
)ENGINE=InnoDB;

-- CommentLikeStatus
CREATE TABLE IF NOT EXISTS `CommentLikeStatus` (
    `CommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    `Status` INT(1) NOT NULL,  -- TODO: three states, like, dislike, neutral
    PRIMARY KEY (`CommentID`, `UserID`)
)ENGINE=InnoDB;

-- Set TODO: maybe redaundant 
CREATE TABLE IF NOT EXISTS `Set` (
    `CommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    PRIMARY KEY (`CommentID`, `UserID`)
)ENGINE=InnoDB;

-- MultiComments -- TODO: to be or not to be
CREATE TABLE IF NOT EXISTS `MultiComments` (
    `MultiCommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    `Content` VARCHAR(140), 
    `ParentCommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`MultiCommentID`)
)ENGINE=InnoDB;

-- Reply1
CREATE TABLE IF NOT EXISTS `Reply1` (
    `CommentID` INT(8) NOT NULL, 
    `MultiCommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`CommentID`, `MultiCommentID`)
)ENGINE=InnoDB;

-- Reply2
CREATE TABLE IF NOT EXISTS `Reply2` (
    `MultiCommentID` INT(8) NOT NULL, 
    `ParentCommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`MultiCommentID`, `ParentCommentID`)
)ENGINE=InnoDB;