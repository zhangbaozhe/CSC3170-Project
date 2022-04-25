----------------
--user sign up--
----------------
--first check username is unique; then insert new values to tale

INSERT INTO 
    `Users`
VALUES
    ('username','password')
WHERE NOT EXISTS
    (SELECT `Username` FROM `Users` WHERE `Username` = 'username');