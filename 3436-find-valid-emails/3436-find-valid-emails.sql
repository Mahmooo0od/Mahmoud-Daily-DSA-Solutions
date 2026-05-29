SELECT * FROM Users
WHERE REGEXP_LIKE(email, '^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$');
order by user_id asc