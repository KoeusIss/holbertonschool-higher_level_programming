-- Task 0x14: Retrive temperatures average from MySQL server
-- Select temperature avergae by city from hbtn_0c_0.temperatures in summer
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
