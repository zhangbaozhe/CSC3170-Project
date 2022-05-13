DELETE FROM `UsersGiveComments`
WHERE `UserID` = %d;

DELETE FROM `Comments`
WHERE `UserID` = %d;

DELETE FROM `CommentLikeStatusAppraiseComments`
WHERE `UserID` = %d;

DELETE FROM `CommentLikeStatus`
WHERE `UserID` = %d;

DELETE FROM `MultiComments`
WHERE `UserID` = %d;

DELETE FROM `Users`
WHERE `UserID` = %d;