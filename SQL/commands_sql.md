# COMANDS
**WARNING**: Comands may vary slightly between different database systems (such as MySQL, PostgreSQL, SQL Server, and Oracle)


### Database
| *Description* | *DBMS* | *Comand* |
|:------|:------|:------|
| Creating a database | MySQL, MariaDB, PostgreSQL | CREATE DATABASE database_name; |
| Removing a database | MySQL, MariaDB, PostgreSQL | DROP DATABASE database_name;|
| Renaming a database | PostgreSQL | ALTER DATABASE database_name RENAME TO new_database_name; |
| Selecting a database | MySQL, MariaDB | USE database_name; |
| Selecting a database | PostgreSQL | \c database_name |
| Displaying the databases | MySQL, MariaDB | SHOW DATABASES; |
| Displaying the databases | PostgreSQL | \l |


### Table
| *Description* | *DBMS* | *Comand* |
|:------|:------|:------|
| Creating a table | MySQL, MariaDB, PostgreSQL | CREATE TABLE table_name (column1 data_type, ...); |
| Create a table with the same structure as another table | MySQL, MariaDB | CREATE TABLE table_name LIKE source_table; |
| Create a table with the same structure as another table | PostgreSQL | CREATE TABLE table_name AS TABLE source_table WITH NO DATA; |
| Removing a table | MySQL, MariaDB, PostgreSQL | DROP TABLE table_name; |
| Displaying tables of a database | MySQL, MariaDB | SHOW TABLES; |
| Displaying tables of a database | PostgreSQL | \d |
| Describing a table | MySQL, MariaDB | DESCRIBE table_name; |
| Describing a table | PostgreSQL | \d table_name |


### Columns
| *Description* | *DBMS* | *Comand* |
|:------|:------|:------|
| Adding new columns | MySQL, MariaDB, PostgreSQL | ALTER TABLE table_name ADD COLUMN new_columns data_type; |
| Removing a column | MySQL, MariaDB, PostgreSQL | ALTER TABLE table_name DROP COLUMN columns; |
| Changing data type of a column | MySQL, MariaDB | ALTER TABLE table_name MODIFY COLUMN column data_type; |
| Changing data type of a column | PostgreSQL | ALTER TABLE table_name ALTER COLUMN column data_type; |
| Setting column as not null| MySQL, MariaDB | ALTER TABLE table_name MODIFY column_name data_type NOT NULL |
| Setting column as not null| PostgreSQL | ALTER TABLE table_name ALTER COLUMN column_name SET NOT NULL |
| Adding auto-incrementing column | MySQL, MariaDB | ALTER TABLE table_name ADD COLUMN column_name INT NOT NULL AUTO_INCREMENT PRIMARY KEY; |
| Changing column to be auto-incrementable | MySQL, MariaDB | ALTER TABLE table_name MODIFY COLUMN column_name INT NOT NULL AUTO_INCREMENT; |
| Setting initial number of the increment | MySQL, MariaDB | ALTER TABLE table_name AUTO_INCREMENT = number; |


### Primary Keys
| *Description* | *DBMS* | *Comand* |
|:------|:------|:------|
| Adding a primary key | MySQL, MariaDB, PostgreSQL | ALTER TABLE table_name ADD PRIMARY KEY (column_name); |
| Adding a primary key while creating a column| MySQL, MariaDB, PostgreSQL | ALTER TABLE table_name ADD COLUMN column_name data_type PRIMARY KEY; |
| Adding a primary composite key |  MySQL, MariaDB, Oracle, PostgreSQL, SQL Server | ALTER TABLE table_name ADD PRIMARY KEY (column_name1, column_name2); |
| Removing a primary key | MySQL, MariaDB | ALTER TABLE table_name DROP FOREIGN KEY fk_orders_customer_id; |
| Removing a primary key | PostgreSQL, SQL Server | ALTER TABLE table_name DROP CONSTRAINT table_name_key; |
| Creating a retriction | MySQL, MariaDB, PostgreSQL | ALTER TABLE table_name ADD UNIQUE (column_name); |


### Foreign Keys
| *Description* | *DBMS* | *Comand* |
|:------|:------|:------|
| Adding a foreign key | MySQL, MariaDB | ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name); |
| Adding a foreign key | PostgreSQL | ALTER TABLE table_name ADD CONSTRAINT fk_key_name FOREIGN KEY (column_name) REFERENCES table_name(column_name); |
| Adding a foreign key while creating a column | MySQL, MariaDB, PostgreSQL | ALTER TABLE table_name ADD COLUMN column_name data_type REFERENCES table_name(column_name); |
| Removing a foreign key| MySQL, MariaDB | ALTER TABLE table_name DROP FOREIGN KEY constraint_name; |
| Removing a foreign key| PostgresSQL, SQL server | ALTER TABLE table_name DROP CONSTRAINT constraint_name; |


### Data
| *Description* | *DBMS* | *Comand* |
|:------|:------|:------|
| Displaying the records from a table | MySQL, MariaDB, PostgreSQL | SELECT column_names FROM table_name; |
| Adding data | MySQL, MariaDB, PostgreSQL | INSERT INTO table_name VALUES (data1, data2, ...), (data1, ...), ... ; |
| Adding data from another table | MySQL, MariaDB, PostgreSQL | INSERT INTO table_name (columns) SELECT columns FROM source_table; |
| Changing values of a column | MySQL, MariaDB, PostgreSQL | UPDATE table_name SET column_name = value; |
| Changing specific values of a column | MySQL, MariaDB, PostgreSQL | UPDATE table_name SET column_name = value WHERE conditions; |
| Deleting all data from a table | MySQL, MariaDB, PostgreSQL | DELETE FROM table_name |
| Deleting specific data from a table | MySQL, MariaDB, PostgreSQL | DELETE FROM table_name WHERE conditions |

### Joins
| *Description* | *DBMS* | *Comand* |
|:------|:------|:------|
| Full join | MySQL, MariaDB, PostgreSQL | SELECT column_names FROM table_name FULL JOIN second_table_name ON table_name.column_key = second_table_name.column_key; |

### View
| *Description* | *DBMS* | *Comand* |
|:------|:------|:------|
| Creates a view | MySQL, MariaDB, PostgreSQL | CREATE VIEW view_name SELECT columns FROM table_name; |
| Deletes a view | MySQL, MariaDB, PostgreSQL | DROP VIEW view_name; |
