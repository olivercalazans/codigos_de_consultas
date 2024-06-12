# COMANDS
**WARNING**: Comands may vary slightly between different database systems (such as MySQL, PostgreSQL, SQL Server, and Oracle)


### Database
| *Comand* | *Description* |
|:------|:------|
| CREATE DATABASE database_name; | Creates a database |
| DROP DATABASE database_name; | Removes a database |
| USE database_name; | Selects a database |
| SHOW DATABASES; | Displays the databases |


### Table
| *Comand* | *Description* |
|:------|:------|
| CREATE TABLE table_name (column1 data_type, ...); | Creates a table |
| DROP TABLE table_name; | Removes a table |
| SHOW TABLES; | Displays the tables of a database |
| ALTER TABLE table_name ADD new_columns data_type; | Adds new columns |
| ALTER TABLE table_name DROP COLUMN columns; | Removes columns
| ALTER TABLE table_name ALTER COLUMN column data_type | Changes data type of a column |


### Data
| *Comand* | *Description* |
|:------|:------|
| SELECT columns FROM table_name; | Displays the records from a table |
| INSERT INTO table_name VALUES (data1, data2, ...), (data1, ...), ... ; | Adds data |
| UPDATE table_name SET column = value; | Changes values of a column |
| UPDATE table_name SET column = value WHERE conditions; | Changes secific values of a column |
| DELETE FROM table_name | Deletes all data from a table |
| DELETE FROM table_name WHERE conditions | Deletes specific data from a table |


### View
| *Comand* | *Description* |
|:------|:------|
| CREATE VIEW view_name SELECT columns FROM table_name; | Creates a view |
| DROP VIEW view_name; | Deletes a view |
