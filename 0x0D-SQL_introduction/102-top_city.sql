-- Task 0x13: Retrive temperatures average from MySQL server
-- Select temperature avergae by city from hbtn_0c_0.temperatures in summer
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month=7 or month=8
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3;
