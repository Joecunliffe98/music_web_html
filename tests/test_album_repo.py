from lib.albumrepo import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/albums_table.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
Album(1, 'album0', 2000, 1),
Album(2, 'album1', 2001, 1),
Album(3, 'album2', 2002, 1),
Album(4, 'album3', 2003, 1),
Album(5, 'album4', 2004, 1)
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)
    assert album == Album(3, 'album2', 2002, 1)

"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, 'album5', 2004, 1))

    result = repository.all()
    assert result == [
Album(1, 'album0', 2000, 1),
Album(2, 'album1', 2001, 1),
Album(3, 'album2', 2002, 1),
Album(4, 'album3', 2003, 1),
Album(5, 'album4', 2004, 1),
Album(6, 'album5', 2004, 1)
    ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
Album(1, 'album0', 2000, 1),
Album(2, 'album1', 2001, 1),
Album(4, 'album3', 2003, 1),
Album(5, 'album4', 2004, 1)
    ]
