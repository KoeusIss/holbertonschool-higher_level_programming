-- Task 0x11: converts into utf8 database in MySQL server
-- Alter the charset coding in a the database hbtn_0c_0
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Alter the charset coding in a the table hbtn_0c_0.first_table
ALTER TABLE `hbtn_0c_0`.`first_table` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Alter the charset coding in a the table hbtn_0c_0.first_table.name
ALTER TABLE `hbtn_0c_0`.`first_table`
MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
