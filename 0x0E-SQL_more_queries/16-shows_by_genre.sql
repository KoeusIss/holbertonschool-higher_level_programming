-- Task 0x10: Queries in MySQL server

-- Lists all shows, and all genres linked to it
SELECT      s.`title`, g.`name`
FROM        `tv_shows` AS s
            INNER JOIN `tv_show_genres` AS sg
                ON s.`id` = sg.`show_id`
                RIGHT JOIN `tv_genres` AS g
                    ON sg.`genre_id` =  g.`id`
ORDER BY    s.`title` ASC,
            g.`name` ASC;
