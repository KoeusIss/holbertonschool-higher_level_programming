-- Task 0x02: Create database and user in MySQL server

-- Creates the database hbtn_Od_2
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- Create user user_0d_2@localhost
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
            IDENTIFIED BY 'user_0d_2_pwd';

-- Grant previleges to the user
GRANT SELECT
          ON `hbtn_0d_2`.*
          TO 'user_0d_2'@'localhost';
