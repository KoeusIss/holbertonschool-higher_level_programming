-- Task 0x0F: Queries in MySQL server

-- Lists all comedy shows
SELECT      s.`title`
FROM        `tv_shows` AS s
            INNER JOIN `tv_show_genres` AS sg
                ON s.`id` = sg.`show_id`
                INNER JOIN `tv_genres` AS g
                    ON sg.`genre_id` =  g.`id`
WHERE       g.`name` = 'Comedy'
ORDER BY    s.`title` ASC;
