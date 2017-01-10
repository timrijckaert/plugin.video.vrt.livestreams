class PlayList(object):
    def __init__(self, channel_id, songs):
        self.channel_id = channel_id
        self.songs = songs

    def __str__(self):
        return "Playlist for channel %s with %s songs" % (self.channel_id, len(self.songs))
