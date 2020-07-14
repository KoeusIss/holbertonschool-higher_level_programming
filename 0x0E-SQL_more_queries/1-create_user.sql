-- Task 0x01: Grant previlges in MySQL server

-- Creates a user user_0d_1@localhost
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
            IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all previleges to user_0d_1@localhost
GRANT ALL PRIVILEGES
                  ON *.*
                  TO 'user_0d_1'@'localhost';
