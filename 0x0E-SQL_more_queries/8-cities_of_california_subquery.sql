--  script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT name,
FROM STATES,
WHERE name = "California",
ORDER BY id ASC;
