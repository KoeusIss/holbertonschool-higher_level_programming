-- Task 0x08: Queries in MySQL server

-- Lists all cities in California
SELECT      `cities`.`id`, `cities`.`name`
FROM        `cities`, `states`
WHERE       `states`.`name` = "California"
ORDER BY    `cities`.`id`;
