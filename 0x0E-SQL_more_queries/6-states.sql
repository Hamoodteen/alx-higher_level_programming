-- sqlsqlsqlsqlsqlsqlsqlsqlsqlsql
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (
	`id` INT DEFAULT 1 NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
