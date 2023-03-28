from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self.connection = connection

    def get(self):
        results = self.connection.execute('SELECT * FROM artists')
        artistlist = []
        for result in results:
            this = Artist(result['id'], result['name'], result['genre'])
            artistlist.append(this)
        return artistlist

    def create(self, artist):
        self.connection.execute(f"INSERT INTO artists (name, genre) VALUES ('{artist.name}', '{artist.genre}');")

    def find(self, id):
        result = self.connection.execute("SELECT * FROM artists WHERE id = %s", [id])
        single = result[0]
        return Artist(id, single["name"], single["genre"])
