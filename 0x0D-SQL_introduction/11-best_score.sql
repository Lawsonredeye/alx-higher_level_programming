-- list scores of the table by name and score in ascending order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
