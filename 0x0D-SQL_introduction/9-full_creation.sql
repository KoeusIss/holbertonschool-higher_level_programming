-- Task 0x09: Crates a table in database in MySQL server
-- Create table hbtn_0c_0.second_table
CREATE TABLE IF NOT EXISTS `second_table`(
    `id` INT,
    `name` VARCHAR(256),
    `score` INT
);

-- Insert multiple records to hbtn_0c_0.second_table
INSERT INTO `second_table`
    (`id`, `name`, `score`)
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
