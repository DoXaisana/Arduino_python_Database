CREATE DATABASE led_status_db;

\c led_status_db

CREATE TABLE led_status (
    id SERIAL PRIMARY KEY,
    status VARCHAR(10) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);