import requests

from resources.lib.utils.playlist import PlayList
from resources.lib.utils.song import Song

BASE_SERVICE_VRT_URL = "http://services.vrt.be/"


def get_playlist_for_channel(channel_id):
    playlist_json = get_json(path="playlist/items/",
                             params={'channel_code': channel_id, 'type': 'SONG'},
                             headers={'Accept': 'application/vnd.playlist.vrt.be.playlist_items_1.0+json'})
    playlist_for_channel = [x["properties"] for x in playlist_json["playlistItems"]]
    artists = [artist[0] for artist in [artist_list[0].values() for artist_list in playlist_for_channel]]
    song_names = [song[0] for song in [song_list[1].values() for song_list in playlist_for_channel]]
    artist_with_song_tuple = zip(artists, song_names)
    return [PlayList(channel_id, Song(tpl[0], tpl[1])) for tpl in artist_with_song_tuple]


def get_picture_url_for_song(song_to_search_image):
    song_json = get_json("music/songs",
                         params={"artist_name": song_to_search_image.artist, "title": song_to_search_image.title},
                         headers={'Accept': 'application/vnd.music.vrt.be.songs_2.0+json'})
    matched_songs = song_json["songs"]
    if len(matched_songs) > 0:
        images_ = matched_songs[0]["images"]
        print images_
        # [0]["url"]
    return matched_songs


def get_json(path, params=None, headers=None):
    if headers is None:
        headers = {}
    if params is None:
        params = {}

    return requests.get("%s%s" % (BASE_SERVICE_VRT_URL, path),
                        params=params,
                        headers=headers).json()


song = get_picture_url_for_song(Song("Madonna", "Like a Virgin"))
print song
