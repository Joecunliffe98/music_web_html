import os
from lib.album import Album
from lib.albumrepo import AlbumRepository
from lib.database_connection import get_flask_database_connection
from lib.ArtistRepository import ArtistRepository
from lib.artist import Artist
from flask import Flask, request, render_template


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)


# GET ALBUMS EXERCISE ROUTE:
@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection()
    repo = AlbumRepository(connection)
    listalbums = repo.all()
    return render_template('albums.html', albums=listalbums)


# GET SINGLE ALBUM EXERCISE ROUTE:
@app.route('/albums/<id>')
def get_single_album(id):
    connection = get_flask_database_connection()
    repo = AlbumRepository(connection)
    alb = repo.find(id)
    artistRepo = ArtistRepository(connection)
    artistid = alb.artist_id
    artist = artistRepo.find(artistid)
    artist_name = artist.name
    return render_template('album.html', album=alb,artist=artist_name)


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


