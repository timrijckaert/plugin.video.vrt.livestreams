import requests

from resources.lib.utils.playlist import PlayList
from resources.lib.utils.song import Song

BASE_SERVICE_VRT_URL = "http://services.vrt.be/"


def get_playlist_for_channel(channel_id):
    playlist_json = get_json(path="playlist/items/",
                             params={'channel_code': channel_id, 'type': 'SONG'},
                             headers={'Accept': 'application/vnd.playlist.vrt.be.playlist_items_1.0+json'})
    playlist_for_channel = [x["properties"] for x in playlist_json["playlistItems"]]
    artists = [a[0] for a in [artist_list[0].values() for artist_list in playlist_for_channel]]
    song_names = [s[0] for s in [song_list[1].values() for song_list in playlist_for_channel]]
    artist_with_song_tuple = zip(artists, song_names)
    songs = [Song(tpl[0], tpl[1], get_itunes_picture_url_for_song(tpl[0], tpl[1])) for tpl in artist_with_song_tuple]
    return PlayList(channel_id, songs)


def get_picture_url_for_song(artist_name, song_title):
    song_json = get_json("music/songs/",
                         params={"artist_name": artist_name, "title": song_title},
                         headers={'Accept': 'application/vnd.music.vrt.be.songs_2.0+json'})
    matched_songs = song_json["songs"]
    if len(matched_songs) > 0:
        matched_song = matched_songs[0]
        if "images" in matched_song:
            matched_song_images = matched_song["images"]
            if len(matched_song_images) > 0 and "url" in matched_song_images[0]:
                return matched_song_images[0]["url"]

    return None


def get_itunes_picture_url_for_song(artist_name, song_title):
    itunes_song_data_request = requests.get("https://itunes.apple.com/search",
                                            params={"term": "%s %s" % (artist_name, song_title),
                                                    "country": "BE",
                                                    "entity": "song",
                                                    "limit": "1"})
    if itunes_song_data_request.ok:
        itunes_song_data_json = itunes_song_data_request.json()
        if int(itunes_song_data_json["resultCount"]) >= 1:
            return itunes_song_data_json["results"][0]["artworkUrl100"].replace("100x100", "500x500")

    return None


def get_json(path, params=None, headers=None):
    if headers is None:
        headers = {}
    if params is None:
        params = {}

    return requests.get("%s%s" % (BASE_SERVICE_VRT_URL, path),
                        params=params,
                        headers=headers).json()
