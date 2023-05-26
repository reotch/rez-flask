DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS education;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(255) UNIQUE NOT NULL,
  password TEXT NOT NULL,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  email VARCHAR(255),
  phone_number VARCHAR(255)
);

CREATE TABLE education (
  education_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  institution VARCHAR(255),
  degree VARCHAR(255),
  start_year INTEGER,
  end_year INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id)
);