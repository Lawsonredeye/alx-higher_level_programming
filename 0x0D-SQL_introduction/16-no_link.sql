-- lists all records of the table second_table of the database hbtn_0c_0
SELECT *
	FROM hbtn_0c_0
	GROUP BY score, name
	ORDER BY score DESC
	WHERE name NOT NULL;
