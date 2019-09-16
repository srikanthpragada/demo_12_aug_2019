CREATE TABLE authors (
    id    INTEGER      PRIMARY KEY AUTOINCREMENT,
    name  VARCHAR (30) NOT NULL,
    email VARCHAR (50) UNIQUE,
    phone VARCHAR (30)
);