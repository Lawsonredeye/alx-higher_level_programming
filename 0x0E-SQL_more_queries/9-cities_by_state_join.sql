--  script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT name
FROM cities
WHERE state_id = (Sel id FROM states WHERE name = "California")
ORDER BY id ASC;
