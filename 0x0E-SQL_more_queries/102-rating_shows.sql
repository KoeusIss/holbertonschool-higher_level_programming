-- Queries in MySQL server
-- Select rating by shows
SELECT s.title, sum(r.rate) AS rating
FROM tv_shows AS s
INNER JOIN tv_show_ratings AS r
ON s.id = r.show_id
GROUP BY s.title
ORDER BY rating DESC;
