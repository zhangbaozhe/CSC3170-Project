DELETE FROM `CommentLikeStatusAppraiseComments`
WHERE `CommentID` = %d;

DELETE FROM `CommentLikeStatusAppraiseComments`
WHERE `CommentID` = %d;

DELETE FROM `UsersSetCommentLikeStatus`
WHERE `CommentID` = %d;

DELETE FROM `MultiComments`
WHERE `ParentCommentID` = %d;

DELETE FROM `MultiCommentsReplyComments`
WHERE `CommentID` = %d;

DELETE FROM `Comments`
WHERE `CommentID` = %d;
