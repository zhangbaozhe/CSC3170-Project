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
    `Semester` VARCHAR(10), -- TODO: finite insertion
    `Year` DATE, -- TODO: only year? 
    `Instructor` VARCHAR(20), -- null?
    `Score` DECIMAL(2,1) NOT NULL, 
    `Content` VARCHAR(140), 
    `LikeNum` INT(5) NOT NULL, 
    `DislikeNum` INT(5) NOT NULL, 
    `Credits` INT(1) NOT NULL, 
    PRIMARY KEY (`CommentID`), 
    FOREIGN KEY (`CourseID`) REFERENCES `Courses` (`CourseID`)
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
    `IsValid` BOOLEAN NOT NULL, 
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
    `Status`,  -- FIXME: need to recheck
    PRIMARY KEY (`CommentID`, `UserID`)
)ENGINE=InnoDB;

-- Set
CREATE TABLE IF NOT EXISTS `Set` (
    `CommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    PRIMARY KEY (`CommentID`, `UserID`)
)ENGINE=InnoDB;

-- MultiComments
CREATE TABLE IF NOT EXISTS `MultiComments` (
    `MultiCommentID` INT(8) NOT NULL, 
    `UserID` INT(8) NOT NULL, 
    `Content` VARCHAR(140), 
    `LowerLevelCommentID` INT(8) NOT NULL, -- TODO: what's this?
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
    `LowerLevelCommentID` INT(8) NOT NULL, 
    PRIMARY KEY (`MultiCommentID`, `LowerLevelCommentID`)
)ENGINE=InnoDB;