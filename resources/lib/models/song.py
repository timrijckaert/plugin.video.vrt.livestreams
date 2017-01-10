class Song(object):
    def __init__(self, artist, title, image_url):
        self.artist = artist
        self.title = title
        self.image_url = image_url

    def __str__(self):
        return "%s - %s" % (self.artist, self.title)
