DELETE FROM `UsersGiveComments`
WHERE `UserID` = {userID};
DELETE FROM `Comments`
WHERE `UserID` = {userID};
DELETE FROM `CommentLikeStatusAppraiseComments`
WHERE `UserID` = {userID};
DELETE FROM `CommentLikeStatus`
WHERE `UserID` = {userID};
DELETE FROM `MultiComments`
WHERE `UserID` = {userID};
DELETE FROM `Users`
WHERE `UserID` = {userID};