# DATA TYPES 
**WARNING**: Data types may vary slightly between different database systems (such as MySQL, PostgreSQL, SQL Server, and Oracle)


### NUMERIC DATA TYPE 
| Data Type | Description |
|:------|:------|
| TINYINT | A small integer |
| SMALLINT | A medium-sized integer | 
| MEDIUMINT | A medium-large integer |
| INT or INTEGER | A standard-sized integer |
| BIGINT | A large integer |
| FLOAT | A single-precision floating-point number |
| DOUBLE or DOUBLE PRECISION | A double-precision floating-point number |
| DECIMAL or NUMERIC | A number with fixed precision and scale, useful for monetary values |


### CHARACTER STRING DATA TYPE
| Data Type | Description |
|:------|:------|
| CHAR | A fixed-length character string |
| VARCHAR | A variable-length character string |
| TEXT | A long text field |
| TINYTEXT, MEDIUMTEXT, LONGTEXT | Variants of TEXT for different lengths of text |


### DATE AND TIME DATA TYPES
| Data Type | Description |
|:------|:------|
| DATETIME | Combines date and time |
| TIMESTAMP | A combination of date and time that can be used for timestamping |
| DATE | A date in the format YYYY-MM-DD |
| TIME | A time in the format HH:MM:SS |
| YEAR | A year in the format YYYY |


### BINARY DATA TYPES
| Data Type | Description |
|:------|:------|
| BINARY | Fixed-length binary data |
| VARBINARY | Variable-length binary data |
| BLOB | A large binary object |
| TINYBLOB, MEDIUMBLOB, LONGBLOB | Variants of BLOB for different sizes of binary data |


### BOOLEAN DATA TYPE
| Data Type | Description |
|:------|:------|
| BOOLEAN or BOOL | A boolean value that can be TRUE or FALSE |


### ENUMERATED AND SET DATA TYPES
| Data Type | Description |
|:------|:------|
| ENUM | An enumerated set of values, where each value must be explicitly listed |
| SET | A set of distinct values, where a column can store any combination of these values |


### OTHER DATA TYPES 
| Data Type | Description |
|:------|:------|
| GEOMETRY, POINT, LINESTRING, POLYGON | Spatial data types to store geographic information |
| JSON | A data type to store JSON-formatted data |


# COMANDS
**WARNING**: Comands may vary slightly between different database systems (such as MySQL, PostgreSQL, SQL Server, and Oracle)


### Database
| *Comand* | *Description* |
|:------|:------|
| CREATE DATABASE database_name; | Creates a database |
| DROP DATABASE database_name; | Removes a database |
| USE database_name;(MySQL/MariDB)<br>\c database_name (PostreSQL) | Selects a database |
| SHOW DATABASES; (MySQL/MariaDB)<br>\l (PostgreSQL) | Displays the databases |


### Table
| *Comand* | *Description* |
|:------|:------|
| CREATE TABLE table_name (column1 data_type, ...); | Creates a table |
| DROP TABLE table_name; | Removes a table |
| SHOW TABLES; (MySQL/MariaDB)<br>\d (PostgreSQL) | Displays the tables of a database |
| ALTER TABLE table_name ADD COLUMN new_columns data_type; | Adds new columns |
| ALTER TABLE table_name DROP COLUMN columns; | Removes a column |
| ALTER TABLE table_name ALTER COLUMN column data_type; | Changes data type of a column |
| ALTER TABLE table_name ADD PRIMARY KEY (column_name); | Adds a primary key |
| ALTER TABLE table_name DROP CONSTRAINT table_name_key; | Removes a primary key |
| ALTER TABLE table_name ADD COLUMN column_name data_type REFERENCES table_name(column_name); | Adds a primary key |
| ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name); | Adds a foreign key |
| ALTER TABLE table_name ADD UNIQUE (column_name); | Creates a retriction |



### Data
| *Comand* | *Description* |
|:------|:------|
| SELECT column_names FROM table_name; | Displays the records from a table |                 
| SELECT column_names FROM table_name FULL JOIN second_table_name ON table_name.column_key = second_table_name.column_key; | Display the records from two tables using keys |
| INSERT INTO table_name VALUES (data1, data2, ...), (data1, ...), ... ; | Adds data |
| UPDATE table_name SET column_name = value; | Changes values of a column |
| UPDATE table_name SET column_name = value WHERE conditions; | Changes secific values of a column |
| DELETE FROM table_name | Deletes all data from a table |
| DELETE FROM table_name WHERE conditions | Deletes specific data from a table |


### View
| *Comand* | *Description* |
|:------|:------|
| CREATE VIEW view_name SELECT columns FROM table_name; | Creates a view |
| DROP VIEW view_name; | Deletes a view |
