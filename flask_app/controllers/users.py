from pprint import pprint
from flask_app import app, render_template, redirect, request, session
from flask_app.model.user import User

# find all albums
@app.get('/albums')
def index():
    print('*********************************')
    print('IN THE /ALBUMS ROUTE')
    print('*********************************')
    albums = Album.find_all()
    print('ALBUMS IN SERVER.PY')
    pprint(albums)
    return render_template('index.html', albums = albums)

# find one album by id
@app.get('/albums/<int:album_id>')
def find_by_id(album_id):
    data = {
        'id': album_id
    }

    album = Album.find_by_id(data)
    return render_template('display_album.html', album = album)

# display form to create album
@app.get('/albums/new')
def new_album():
    return render_template('new_album.html')

# create an album
@app.post('/albums')
def create_album():
    data = {
        'title': request.form['title'],
        'artist': request.form['artist'],
        'description': request.form['description']
    }
    album_id = Album.save(data)
    print(f'CREATED ALBUM WITH ID: {album_id}')
    return redirect('/albums')

# display form to edit album
@app.get('/albums/<int:album_id>/edit')
def edit_album(album_id):
    data = {
        'id': album_id
    }

    album = Album.find_by_id(data)
    return render_template('edit_album.html', album = album)

# update an album
@app.post('/albums/<int:album_id>/update')
def update_album(album_id):
    data = {
        'id': album_id,
        'title': request.form['title'],
        'artist': request.form['artist'],
        'description': request.form['description']
    }
    Album.find_by_id_and_update(data)
    return redirect(f'/albums/{album_id}')

# delete route
@app.get('/albums/<int:album_id>/delete')
def delete_album(album_id):
    data = {
        'id': album_id
    }
    Album.find_by_id_and_delete(data)
    return redirect('/albums')