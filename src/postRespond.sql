INSERT INTO `MultiComments` 
(`UserID`, `Content`,`ParentCommentID`)
VALUES
(%s, %s, %s);

SELECT `MultiCommentID`
FROM `MultiComments`
WHERE `UserID` = %s AND `ParentCommentID` = %s;

INSERT INTO `MultiCommentsReplyComments` (
`CommentID`,`MultiCommentID`)
VALUES 
(%s,%s);
