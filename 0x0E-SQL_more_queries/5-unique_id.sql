-- Create table in MySQL server

-- Create table hbtn_0d_0.unique_id
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`    INT DEFAULT 1 UNIQUE,
    `name`  VARCHAR(256)
);
