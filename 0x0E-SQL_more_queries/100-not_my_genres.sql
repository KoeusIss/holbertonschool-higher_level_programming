-- Task 0x11: Queries in MySQL server
-- Lists genres not linked to "Dexter" tv show
SELECT DISTINCT     g.name
FROM                tv_genres               AS g
    INNER JOIN      tv_show_genres          AS sg
        ON g.id = sg.genre_id
        INNER JOIN tv_shows                 AS s
            ON sg.show_id = s.id
WHERE g.name NOT IN (
    SELECT          g.name 
    FROM            tv_genres               AS g
        INNER JOIN tv_show_genres           AS sg
            ON g.id = sg.genre_id
            INNER JOIN tv_shows             AS s
                ON sg.show_id = s.id
    WHERE s.title = "Dexter"
)
ORDER BY g.`name` ASC;
