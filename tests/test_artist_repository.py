from lib.ArtistRepository import ArtistRepository
from lib.artist import Artist

# When we call .get() on our artistreopository, we get a list of all the artist objects as a string

def test_get_all_records(db_connection):
    db_connection.seed("seeds/albums_table.sql") 
    repository = ArtistRepository(db_connection)
    assert repository.get() == [
    Artist(1, 'Pixies', 'Alternative'), 
    Artist(2, 'ABBA', 'pop'),
    Artist(3, 'Taylor Swift', 'pop'),
    Artist(4, 'Nina Simone', 'Jazz'),
    Artist(5, 'Wild Nothing', 'Indie')]

# When we call create with an artist name and genre, the artist is added to the database

def test_can_create(db_connection):
    db_connection.seed("seeds/albums_table.sql") 
    repository = ArtistRepository(db_connection)
    newArtist = Artist(None, 'Linkin Park', 'Alternative')
    repository.create(newArtist)
    assert repository.get() == [
    Artist(1, 'Pixies', 'Alternative'), 
    Artist(2, 'ABBA', 'pop'),
    Artist(3, 'Taylor Swift', 'pop'),
    Artist(4, 'Nina Simone', 'Jazz'),
    Artist(5, 'Wild Nothing', 'Indie'),
    Artist(6, 'Linkin Park', 'Alternative')]

# Can locate artist by artist id

def test_find_artist_by_id(db_connection):
    db_connection.seed("seeds/albums_table.sql") 
    repository = ArtistRepository(db_connection)
    assert repository.find(1) == Artist(1, 'Pixies', 'Alternative')
