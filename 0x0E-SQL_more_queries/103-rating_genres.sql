-- Queries in MySQL server
-- Lists all genres by their rating
SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
INNER JOIN tv_shows AS s
ON sg.show_id = s.id
INNER JOIN tv_show_ratings AS r
ON s.id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
