SELECT * FROM `MultiComments`,`Users`
WHERE `ParentCommentID` = '%s'
and Multicomments.UserID = Users.UserID;
