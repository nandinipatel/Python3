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

        self.name = title
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
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)

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

        self.albums.append(album)
    
    def add_song(self, name, year, title):
        """Add a new song to the collection of albums

        This method will add the song to an album in the collection.
        
        Args:
            name(str): The name of the album
            year(int): The year of the album was produced
            title(str): The titel of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print("Found album " + name)
        album_found.add_song(title)

def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None

def load_data():
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            #row consists of artist, album, year, song
            artist, album, year, song = tuple(line.strip('\n').split('\t'))
            year = int(year)
            print("{}:{}:{}:{}".format(artist, album, year, song))

            new_artist = find_object(artist, artist_list)
            if new_artist is None:
                new_artist = Artist(artist)
                artist_list.append(new_artist)

            new_artist.add_song(album, year, song)
    return artist_list

def create_checkfile(artist_list):
    """Create a check file from the object data for comparision with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song), file=checkfile)
    
if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)