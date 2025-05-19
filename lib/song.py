class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level tracking
        self.add_song_to_count()
        self.add_to_artists()
        self.add_to_genres()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls, artist=None):
        artist = artist or cls.artist
        if artist not in cls.artists:
            cls.artists.append(artist)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1


s1 = Song("99 Problems", "Jay-Z", "Rap")
s2 = Song("God's Plan", "Drake", "Rap")
s3 = Song("Halo", "Beyonce", "Pop")
s4 = Song("Formation", "Beyonce", "Pop")

print(Song.count)
# => 4

print(Song.artists)
# => ['Jay-Z', 'Drake', 'Beyonce']

print(Song.genres)
# => ['Rap', 'Pop']

print(Song.genre_count)
# => {'Rap': 2, 'Pop': 2}

print(Song.artist_count)
# => {'Jay-Z': 1, 'Drake': 1, 'Beyonce': 2}
