DROP TABLE users;
CREATE TABLE users (
    user_id INTEGER NOT NULL,
    name TEXT,
    sex TEXT,
    birthday TEXT,
    city TEXT,
    country TEXT,
    PRIMARY KEY (user_id)
)
()
COMMIT
INSERT INTO users (user_id, name, sex, birthday, city, country) VALUES (?, ?, ?, ?, ?, ?)
(
    (1, 'Jack', 'M', NULL, 'Kanzas', 'USA'),
    (2, 'Mike', 'M', NULL, 'San Antonio', 'USA'),
    (3, 'Tokishi', 'F', NULL, 'Kyoto', 'Japan'),
    (4, 'Vasya', 'M', NULL, 'Arzamas', 'Russia')
)
()
COMMIT
