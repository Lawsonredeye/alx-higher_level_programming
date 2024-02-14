# 0x0D-SQL_introduction

Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology you’re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology you’re using is stateless or stateful, you will need to persist your data somewhere. That’s what databases are for.

## DDL (Data Definition Language):

DDL is used to define the structure of the database.
It includes commands such as CREATE, ALTER, DROP, and TRUNCATE.
Example: CREATE TABLE, ALTER TABLE ADD COLUMN, DROP TABLE.

## DML (Data Manipulation Language):

DML deals with the manipulation of data stored in the database.
Common commands include SELECT, INSERT, UPDATE, and DELETE.
Example: INSERT INTO, UPDATE SET, DELETE FROM.

## MySQL
MySQL is a popular relational database management system. In this chapter, we'll learn how to create a database.

### Step 1: Access MySQL

Firstly, log in to MySQL with administrative privileges. Open your terminal and enter the following command, replacing [username] with your MySQL username:

`mysql -u [username] -p`

You'll be prompted to enter your MySQL password.

### Step 2: Create a Database

To create a new database, use the following SQL command:
`CREATE DATABASE your_database_name;`

Replace your_database_name with the desired name for your database.

### Step 3: Verify Database Creation

To confirm the creation of your database, you can list all databases:
`SHOW DATABASES;`
