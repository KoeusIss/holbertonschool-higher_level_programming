-- Task 0x08: Queries in MySQL server

-- Lists all cities in California
SELECT DISTINCT `cities`.`id`, `cities`.`name`
FROM            `cities`, `states`
WHERE           `cities`.`state_id` =
(
    SELECT  `states`.`id`
    FROM    `states`
    WHERE   `states`.`name` = "California"
)
ORDER BY    `cities`.`id` ASC;
