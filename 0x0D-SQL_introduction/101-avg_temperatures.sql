-- Task 0x12: Retrive temperatures average from MySQL server
-- Select temperature avergae by city from hbtn_0c_0.temperatures
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC
