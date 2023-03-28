-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums CASCADE;
DROP SEQUENCE IF EXISTS albums_id_seq;

DROP TABLE IF EXISTS artists CASCADE;
DROP SEQUENCE IF EXISTS artists_id_seq;

CREATE TABLE artists (
id SERIAL PRIMARY KEY,
name text,
genre text
);

-- Then, we recreate them
CREATE TABLE albums (
id SERIAL PRIMARY KEY,
title text,
release_year int,
artist_id int, 
constraint fk_artists foreign key(artist_id)
        references artists(id)
        on delete cascade
);

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Alternative');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');
INSERT INTO artists (name, genre) VALUES ('Wild Nothing', 'Indie');

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('album0', '2000', 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('album1', '2001', 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('album2', '2002', 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('album3', '2003', 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('album4', '2004', 1);










