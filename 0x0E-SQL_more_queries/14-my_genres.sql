-- Task 0x0E: Queries in MySQL server

-- Select all genres for the show "Dexter"
SELECT      g.`name`
FROM        `tv_genres` AS g
                INNER JOIN `tv_show_genres` AS sg
                    ON g.`id` = sg.`genre_id`
                    INNER JOIN `tv_shows` AS s
                        ON sg.`show_id` = s.`id`
WHERE       s.`title` = 'Dexter'
ORDER BY    g.`name` ASC;
