-- Task 0x0F: Lists number of record in MySQL server
-- Lists number of record with the same score in hbtn_0c_0.second_table
SELECT `score`, COUNT(`name`) `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC;
