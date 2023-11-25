-- This is a placeholder SQL schema file. Actual schema will depend on the project requirements.

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS game_data (
    id INT AUTO_INCREMENT,
    user_id INT,
    game_state JSON,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);