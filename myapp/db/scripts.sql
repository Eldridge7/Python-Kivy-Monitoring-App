CREATE DATABASE IF NOT EXISTS app_db;
USE app_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user'

);

CREATE TABLE IF NOT EXISTS keylogger (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    log LONGTEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS cliplogger (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    log LONGTEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS screenlogger (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    log LONGTEXT, -- You might want to adjust this to fit the kind of data you will be storing
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


-- ALTER TABLE keylogger
-- MODIFY COLUMN log LONGTEXT;

-- ALTER TABLE cliplogger
-- MODIFY COLUMN log LONGTEXT;

-- ALTER TABLE screenlogger
-- MODIFY COLUMN log LONGTEXT;

-- SELECT T_01.*
-- FROM userinfo.User_Logon_Recency T_01
-- WHERE (
--      T_01.maxLogonTime < ((current_date - 90) (Timestamp(6)))
--      OR
--      T_01.maxLogonTime IS NULL
--      )
-- ;