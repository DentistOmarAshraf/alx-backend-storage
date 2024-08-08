-- Create table users

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL auto_increment PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
)