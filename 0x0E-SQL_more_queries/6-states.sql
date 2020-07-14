-- Task 0x06: Create table and database in MySQL server

-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create table hbtn_0d_usa.states
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    `id`    INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    `name`  VARCHAR(256) NOT NULL
);
