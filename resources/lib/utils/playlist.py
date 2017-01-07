class PlayList(object):
    def __init__(self, channel_id, song):
        self.channel_id = channel_id
        self.song = song

    def __str__(self):
        return "%s" % self.song
