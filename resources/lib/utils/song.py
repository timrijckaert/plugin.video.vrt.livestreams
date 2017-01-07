class Song(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    def __str__(self):
        return "%s - %s" % (self.artist, self.title)
