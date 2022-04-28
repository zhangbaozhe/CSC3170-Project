# User account-LYY

1. sign up insert `users`
2. change password `users`
3. todo: retrieve password
4. login `users`

# Search-LJX

1. simple filter `courses` & `Evaluate` (let user choose form pre-defiened tags)
2. jump to `comment` (simple query)
3. *todo: advanced search*

# User center-YYQ

1. simple query **my comments** `comment`

2. simple query **my like** `comment`

3. complex query **Like Me**: show a table with 2 attributes: "username" & "comment content"

   `appraise` `comment_like_status` `comment`

# Comment display-ZBZ(234)-LYY(1)

1. simply display all the comments `comments` `comment_like_status`

2. create new comment `comments`

3. like/dislike a comment:

   step1: query `comment_like_status` with user_id

   step2: update/create `comment_like_status` (`set`?)

   step3: update `comments`, `appraise`

4. create child comment:

   step1: create in `comments` and `reply1`