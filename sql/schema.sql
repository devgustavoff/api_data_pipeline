CREATE TABLE weather_readings (
    name VARCHAR,
    temperature REAL,
    humidity INT,
    description VARCHAR,
    collected_at TIMESTAMP,
    UNIQUE (name, collected_at)
);