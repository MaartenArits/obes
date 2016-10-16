import shutil, os
from django.utils import timezone
from .media_objects import Movie, MediaLibrary, AudioBook, Album


def addMovie(request, toAddMediaLocation, mediaLibraryLocation):
    name = request.POST['name']
    year = request.POST['year']
    global_id = request.POST['global_id']
    age = request.POST['age']
    genres = request.POST['genres']
    explanation = request.POST['explanation']
    trailer = request.POST['trailer_path']
    art = request.POST['art_path']
    movie = request.POST['movie_path']
    owner = request.POST['owner']

    working_directory = mediaLibraryLocation + 'movies/' + name + '/'

    createMovieTree(working_directory)
    copyMovieFiles(art, movie, trailer, working_directory)
    createMovieMetaFile(age, art, explanation, genres, global_id, movie, name, owner, trailer, working_directory, year)

    if 'delete_original' in request.POST:
        deleteOldMovieFiles(movie, toAddMediaLocation)


def deleteOldMovieFiles(movie, toAddMediaLocation):
    formated_dir = movie.split('/', len(toAddMediaLocation.split('/')))[-1]
    path_list = formated_dir.split('/')
    old_folder_location = path_list[0]

    shutil.rmtree(toAddMediaLocation + '/movies/' + old_folder_location)


def createMovieMetaFile(age, art, explanation, genres, global_id, movie, name, owner, trailer, working_directory, year):
    movie_location = working_directory + 'movie/' + movie.split('/')[-1]
    art_location = working_directory + 'art/' + art.split('/')[-1]
    trailer_location = working_directory + 'trailer/' + trailer.split('/')[-1]
    movieObject = Movie(name, year, owner, timezone.now(), global_id, age, genres, explanation, movie_location,
                        trailer_location, art_location)

    with open(working_directory + 'meta', 'wb+') as outfile:
        outfile.write(movieObject.get_json())


def copyMovieFiles(art, movie, trailer, working_directory):
    shutil.copy(art, working_directory + 'art/')
    shutil.copy(movie, working_directory + 'movie/')
    shutil.copy(trailer, working_directory + 'trailer/')


def createMovieTree(working_directory):
    os.mkdir(working_directory, 0755)
    os.mkdir(working_directory + 'art/', 0755)
    os.mkdir(working_directory + 'movie/', 0755)
    os.mkdir(working_directory + 'trailer/', 0755)


def searchToAddMovies(toAddMediaLocation):
    toAddMediaLibrary = MediaLibrary()

    activeMovie = ''
    currentMovie = ''
    art_location = []
    video_location = []
    for dirname, dirnames, filenames in os.walk(toAddMediaLocation + 'movies/'):
        for filename in filenames:

            formated_dir = dirname.split('/', len(toAddMediaLocation.split('/')))[-1]
            path_list = formated_dir.split('/')
            currentMovie = path_list[0]
            if currentMovie != activeMovie:
                if activeMovie != '':
                    toAddMediaLibrary.add_movie(activeMovie, '', '', timezone.now(), '', '', '', '',
                                                video_location, video_location, art_location)
                art_location = []
                video_location = []
                activeMovie = currentMovie

            file_extention = filename.split('.')[-1]
            if file_extention == 'jpg':
                art_location.append(os.path.join(dirname, filename))

            if file_extention == 'mp4':
                video_location.append(os.path.join(dirname, filename))
    if activeMovie != '' and activeMovie == currentMovie:
        toAddMediaLibrary.add_movie(activeMovie, '', '', timezone.now(), '', '', '', '',
                                    video_location, video_location, art_location)

    return toAddMediaLibrary


def addAudiobook(request, toAddMediaLocation, mediaLibraryLocation):
    name = request.POST['name']
    year = request.POST['year']
    global_id = request.POST['global_id']
    owner = request.POST['owner']
    language = request.POST['language']
    explanation = request.POST['explanation']
    publisher = request.POST['publisher']
    narrator = request.POST['narrator']
    author = request.POST['author']
    audiobook = request.POST['book_path']
    art = request.POST['art_path']

    working_directory = mediaLibraryLocation + 'audiobooks/' + name + '/'

    createAudiobookTree(working_directory)
    copyAudiobookFiles(art, audiobook, working_directory)
    createAudiobookMetaFile(name, year, owner, timezone.now(), global_id, language, explanation, publisher,
                            narrator, author, audiobook, art, working_directory)

    if 'delete_original' in request.POST:
        deleteOldAudiobookFiles(audiobook, toAddMediaLocation)


def deleteOldAudiobookFiles(audiobook, toAddMediaLocation):
    formated_dir = audiobook.split('/', len(toAddMediaLocation.split('/')))[-1]
    path_list = formated_dir.split('/')
    old_folder_location = path_list[0]

    shutil.rmtree(toAddMediaLocation + '/audiobooks/' + old_folder_location)


def createAudiobookMetaFile(name, year, owner, creation_date, global_id, language, explanation, publisher,
                            narrator, author, audiobook, art, working_directory):
    audiobook = working_directory + 'audiobook/' + audiobook.split('/')[-1]
    art = working_directory + 'art/' + art.split('/')[-1]
    audiobookObject = AudioBook(name, year, owner, creation_date, global_id, language, explanation, publisher,
                                narrator, author, audiobook, art)

    with open(working_directory + 'meta', 'wb+') as outfile:
        outfile.write(audiobookObject.get_json())


def copyAudiobookFiles(art, audiobook, working_directory):
    shutil.copy(art, working_directory + 'art/')
    shutil.copy(audiobook, working_directory + 'audiobook/')


def createAudiobookTree(working_directory):
    os.mkdir(working_directory, 0755)
    os.mkdir(working_directory + 'art/', 0755)
    os.mkdir(working_directory + 'audiobook/', 0755)


def searchToAddAudiobooks(toAddMediaLocation):
    toAddMediaLibrary = MediaLibrary()

    activeAudiobook = ''
    currentAudiobook = ''
    art_location = []
    audiobook_location = []
    for dirname, dirnames, filenames in os.walk(toAddMediaLocation + 'audiobooks/'):
        for filename in filenames:
            formated_dir = dirname.split('/', len(toAddMediaLocation.split('/')))[-1]
            path_list = formated_dir.split('/')
            currentAudiobook = path_list[0]
            if currentAudiobook != activeAudiobook:
                if activeAudiobook != '':
                    toAddMediaLibrary.add_audiobook(activeAudiobook, '', '', timezone.now(), '', '', '', '',
                                                    '', '', audiobook_location, art_location)
                art_location = []
                audiobook_location = []
                activeAudiobook = currentAudiobook

            file_extention = filename.split('.')[-1]
            if file_extention == 'jpg':
                art_location.append(os.path.join(dirname, filename))

            if file_extention == 'mp3':
                audiobook_location.append(os.path.join(dirname, filename))
    if activeAudiobook != '' and activeAudiobook == currentAudiobook:
        toAddMediaLibrary.add_audiobook(activeAudiobook, '', '', timezone.now(), '', '', '', '',
                                        '', '', audiobook_location, art_location)

    return toAddMediaLibrary


def searchToAddMusic(toAddMediaLocation):
    toAddMediaLibrary = MediaLibrary()

    activeAlbum = ''
    currentAlbum = ''

    art_location = []
    music_location = []

    for dirname, dirnames, filenames in os.walk(toAddMediaLocation + 'music/'):
        for filename in filenames:
            formated_dir = dirname.split('/', len(toAddMediaLocation.split('/')))[-1]
            path_list = formated_dir.split('/')
            currentAlbum = path_list[0]

            if currentAlbum != activeAlbum:
                if activeAlbum != '':
                    toAddAlbum = Album(activeAlbum, '', '', timezone.now(), '', '', '', art_location, '')

                    for number, location in enumerate(music_location):
                        song = location.split('/')[-1]
                        song = song.split('.')[0]
                        toAddAlbum.add_music(song, location, number)

                    toAddMediaLibrary.add_album_object(toAddAlbum)

                art_location = []
                music_location = []
                activeAlbum = currentAlbum

            file_extention = filename.split('.')[-1]
            if file_extention == 'jpg':
                art_location.append(os.path.join(dirname, filename))

            if file_extention == 'mp3':
                music_location.append(os.path.join(dirname, filename))

    if activeAlbum != '' and activeAlbum == currentAlbum:
        toAddAlbum = Album(activeAlbum, '', '', timezone.now(), '', '', '', art_location, '')

        for number, location in enumerate(music_location):
            song = location.split('/')[-1]
            song = song.split('.')[0]
            toAddAlbum.add_music(song, location, number)

        toAddMediaLibrary.add_album_object(toAddAlbum)

    return toAddMediaLibrary


def addMusic(request, toAddMediaLocation, mediaLibraryLocation):
    name = request.POST['name']
    year = request.POST['year']
    owner = request.POST['owner']
    global_id = request.POST['global_id']
    artist = request.POST['artist']
    record_label = request.POST['record_label']
    art_path = request.POST['art_path']
    genres = request.POST['genres']
    creation_date = timezone.now()

    working_directory = mediaLibraryLocation + 'music/' + name + '/'

    temp_music_album = Album(name, year, owner, creation_date, global_id, artist, record_label, art_path, genres)
    amount_of_songs_to_check = request.POST['amount_of_songs']

    temp_music_album = find_enabled_songs(amount_of_songs_to_check, request, temp_music_album)

    createMusicTree(working_directory, temp_music_album)
    copyMusicFiles(working_directory, temp_music_album, temp_music_album.get_art_path())
    createMusicMetaFiles(art_path, artist, creation_date, genres, global_id, name, owner, record_label,
                         temp_music_album, working_directory, year)


def createMusicMetaFiles(art_path, artist, creation_date, genres, global_id, name, owner, record_label,
                         temp_music_album, working_directory, year):
    music_meta_locations = []
    for music in temp_music_album.get_music():
        with open(working_directory + music.get_song_name() + '/' + 'meta', 'wb+') as outfile:
            outfile.write(music.get_json())
        music_meta_locations += [working_directory + music.get_song_name() + '/meta']

    temp_music_album = Album(name, year, owner, creation_date, global_id, artist, record_label, art_path, genres)
    temp_music_album.add_music_object(music_meta_locations)

    with open(working_directory + 'meta', 'wb+') as outfile:
        outfile.write(temp_music_album.get_json())


def find_enabled_songs(amount_of_songs_to_check, request, temp_music_album):
    for song_index in range(0, int(amount_of_songs_to_check)):

        if 'enable_song.' + str(song_index) in request.POST:
            temp_music_album.add_music(request.POST['song_name.' + str(song_index)],
                                       request.POST['music_path.' + str(song_index)],
                                       request.POST['song_number.' + str(song_index)])

    return temp_music_album


def createMusicTree(working_directory, album):
    os.mkdir(working_directory, 0755)
    os.mkdir(working_directory + 'art/', 0755)
    for music in album.get_music():
        os.mkdir(working_directory + music.get_song_name() + '/', 0755)


def copyMusicFiles(working_directory, temp_music_album, art):
    # shutil.copy(art, working_directory + 'art/')
    for music in temp_music_album.get_music():
        shutil.copy(music.get_music_path(), working_directory + music.get_song_name() + '/')
    None
