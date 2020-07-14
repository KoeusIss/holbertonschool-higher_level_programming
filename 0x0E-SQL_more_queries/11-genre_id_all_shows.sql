-- Task 0x0B: Queries in MySQL server

-- Lists all the shows contained in hbtn_0d_tvshows
SELECT      `tv_shows`.`title`, `tv_show_genres`.`genre_id`
FROM        `tv_shows`
LEFT JOIN   `tv_show_genres`
ON          `tv_show_genres`.`show_id` = `tv_shows`.`id`
ORDER BY    `tv_shows`.`title` ASC,
            `tv_show_genres`.`genre_id` ASC;
