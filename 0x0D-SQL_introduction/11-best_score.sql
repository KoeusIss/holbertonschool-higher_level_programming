-- Task 0x0B: lists all the record of table in MySQL server
-- Select customize best score row of hbtn_0c_0.second_table
SELECT `score`, `name`
FROM `second_table`
WHERE `score`>=10
ORDER BY `score` DESC;
