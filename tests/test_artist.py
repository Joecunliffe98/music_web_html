from lib.artist import Artist


# When I construct an artist, it has an ID, name, and genre:

def test_artist_constructs():
    testartist = Artist(1, 'Pixies', 'Alternative')
    assert testartist.id == 1
    assert testartist.name == 'Pixies'
    assert testartist.genre == 'Alternative'  


# When I print an artist, I get a readable string:

def test_artist_strings_well():
    testartist = Artist(1, 'Pixies', 'Alternative')
    assert str(testartist) == 'Artist(1, Pixies, Alternative)'  


# When I construct two identical artists, they are equatable:

def test_artists_equate():
    testartist = Artist(1, 'Pixies', 'Alternative')
    testartist2 = Artist(1, 'Pixies', 'Alternative')
    assert testartist == testartist2