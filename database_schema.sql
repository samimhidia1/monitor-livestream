CREATE TABLE streams (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    url VARCHAR(255)
);

CREATE TABLE keywords (
    id SERIAL PRIMARY KEY,
    word VARCHAR(255) UNIQUE
);

CREATE TABLE alerts (
    id SERIAL PRIMARY KEY,
    stream_id INT REFERENCES streams(id),
    keyword_id INT REFERENCES keywords(id),
    timestamp TIMESTAMP,
    FOREIGN KEY (stream_id) REFERENCES streams(id),
    FOREIGN KEY (keyword_id) REFERENCES keywords(id)
);
