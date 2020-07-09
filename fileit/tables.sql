CREATE TABLE imageittable(
    imageid UUID PRIMARY KEY,
    imagelink TEXT NOT NULL,
    uploadtime TIMESTAMP DEFAULT current_timestamp
);