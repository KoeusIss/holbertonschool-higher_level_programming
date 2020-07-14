-- Task 0x07: Create table and database in MySQL server

-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create table hbtn_0d_usa.cities
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    `id`        INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    `state_id`  INT NOT NULL,
    `name`      VARCHAR(256) NOT NULL,
    FOREIGN KEY (`state_id`) REFERENCES hbtn_0d_usa.states(`id`)
);
