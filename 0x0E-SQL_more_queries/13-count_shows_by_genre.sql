-- Task 0x0D: Queries in MySQL server

-- Lists all genres from hbtn_0d_tvshows with number of shows
SELECT      `tv_genres`.`name`  AS genre,
            COUNT(*)            AS number_of_shows
FROM        `tv_genres`
                INNER JOIN `tv_show_genres`
                    ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
GROUP BY    `tv_genres`.`name`
ORDER BY    number_of_shows DESC;
