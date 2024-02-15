-- Script to convert hbtn_0c_0 database to UTF8MB4
SELECT default_character_set_name FROM information_schema.SCHEMATA 
WHERE schema_name = "hbtn_0c_0";
SELECT CCSA.character_set_name FROM information_schema.`TABLES` T,
       information_schema.`COLLATION_CHARACTER_SET_APPLICABILITY` CCSA
WHERE CCSA.collation_name = T.table_collation
  AND T.table_schema = "hbtn_0c_0"
  AND T.table_name = "first_table";

SELECT character_set_name FROM information_schema.`COLUMNS` 
WHERE table_schema = "hbtn_0c_0"
  AND table_name = "first_table"
  AND column_name = "name";
