# song.py

class Song:
    """
    Represents a song in the music library.

    Tracks both instance-level details (name, artist, genre)
    and class-level statistics for analytics:
    - Total number of songs
    - List of unique artists and genres
    - Count of songs per genre and per artist
    """

    # Class attributes for global tracking
    count = 0                # Total number of Song instances
    genres = []              # Unique list of genres
    artists = []             # Unique list of artists
    genre_count = {}         # Count of songs per genre
    artist_count = {}        # Count of songs per artist

    def __init__(self, name, artist, genre):
        """
        Initialize a new Song instance and update class-level statistics.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update global stats automatically
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # -------------------------
    # Class methods for tracking
    # -------------------------

    @classmethod
    def add_song_to_count(cls):
        """Increment total number of songs."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add genre to the list of unique genres (no duplicates)."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add artist to the list of unique artists (no duplicates)."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the number of songs for the given genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increment the number of songs for the given artist."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1