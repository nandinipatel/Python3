#Author: Nandini Patel
#Date: May 11, 2020
#Description: DocString 

class Song:
    """Class to represent a song

    Attributes:
        title(str): Title of the song
        artist(Artist): An artist object repr. the songs creator
        duration(int): The duration of the song in seconds
    """

    def __init__(self, title, artist, duration=0):
        """ Song init method

        Args:
            title(str): Initialise the 'title' attribute
            artist(Artist): At Artist object, repr. the song creator
            duration(Optional[int]): Initial value for the 'duration' attribute
        """

        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent an Album, using it's track list
    
    Attributes:
        album_name(str): The name of the album
        year(int): The year album was released
        artist(Artist): The artist responsible 
        tracks(List[Song]): A list of the songs on the album

    Methods:
        addSong: Used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = year
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            songs(Song): A song to add
            position(Optional[int]): The song will be added to that position
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:
    """Basic class to store artist details.

    Attributes:
        name(str): The name of the artists
        albums(List[Album]): A list of the albums by this artist
            The list includes only those albums in this collection, it is
            not an exhastive list of the artist' published albums.

    Methods:
        add_album: To add a new album
    """

    def __init__(self, name):
        self.name = name
        self.albums = []
    
    def add_album(self, album):
        """Add a new album to the list

        Args:
            album(Album): Albumn object to add
                Don't add repeated albums!
        """

        self.album.append(album)

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", 'r') as albums:
        for line in albums:
            #row consists of artist, album, year, song
            artist, album, year, song = tuple(line.strip('\n').split('\t'))
            year = int(year)
            print(artist, album, year, song)
    
if __name__ == "__main__":
    load_data()