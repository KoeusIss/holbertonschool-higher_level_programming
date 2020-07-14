-- Task 0x09: Queries in MySQL server

-- Lists all cities in htbn_0d_usa
SELECT          `cities`.`id`, `cities`.`name`, `states`.`name`
FROM            `cities`
INNER JOIN      `states`
ON              `cities`.`state_id` = `states`.`id`
ORDER BY        `cities`.`id` ASC;
