class playlist:
    
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def display_list(self):
        xiter = iter(self.songs)
        while True:
            try:
                wert = next(xiter)
            except StopIteration:
                 break
            print(wert)

newlist = playlist("Meine Lieblingssongs")
newlist.add_song("Song 1")  
newlist.add_song("Song 2")  
newlist.display_list()
