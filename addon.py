import sys
import urllib
import urlparse

import xbmc
import xbmcgui
import xbmcplugin
from resources.lib.utils.playlist_fetcher import get_playlist_for_channel
from resources.lib.utils.radiochannel import get_all_radio_channels
from resources.lib.utils.videochannel import get_all_video_channels

self = sys.argv[0]
handle = int(sys.argv[1])
qs = sys.argv[2]

DEBUG_LOG = "plugin.video.vrt.livestreams :::: "
IS_IN_DEBUG = False
if IS_IN_DEBUG:
    from resources.lib.utils.debugger import start_debugger

    start_debugger()


def create_qs(url_params):
    return self + '?' + urllib.urlencode(url_params)


def get_radio_list_items():
    radio_items = []
    for channel in get_all_radio_channels():
        live_stream_title = channel.title
        live_stream_url = create_qs({
            'url': channel.url,
            'channel_code': channel.channel_code
        })
        list_item = xbmcgui.ListItem(label=live_stream_title,
                                     iconImage=channel.thumbnail_picture,
                                     thumbnailImage=channel.thumbnail_picture,
                                     path=live_stream_url)

        # list_item.setInfo(type='music', infoLabels={
        #     "title": songs[0].title,
        #     "artist": songs[0].artist
        # })
        list_item.setLabel2(channel.description)
        # list_item.setProperty("isPlayable", 'true')
        radio_items.append((live_stream_url, list_item))
    return radio_items


def get_video_list_items():
    video_items = []
    for channel in get_all_video_channels():
        live_stream_title = channel.title
        live_stream_url = channel.video_url
        list_item = xbmcgui.ListItem(label=live_stream_title,
                                     iconImage=channel.thumbnail_picture,
                                     thumbnailImage=channel.thumbnail_picture,
                                     path=live_stream_url)
        list_item.setInfo(type='video', infoLabels={"title": live_stream_title})
        list_item.setProperty("fanart_image", channel.fanart_picture)
        list_item.setProperty("isPlayable", 'true')
        video_items.append((live_stream_url, list_item))
    return video_items


def display_generic_playable_items(items):
    xbmcplugin.addDirectoryItems(handle=handle, items=items, totalItems=len(items))
    xbmcplugin.endOfDirectory(handle, True)


if len(qs) > 1:
    params = urlparse.parse_qs(qs[1:])
    xbmc.log("%s Params %s" % (DEBUG_LOG, params))
    if "content_type" in params:
        if params["content_type"][0] == "video":
            display_generic_playable_items(get_video_list_items())
        else:
            display_generic_playable_items(get_radio_list_items())

    if "url" in params:
        xbmc.log(str(params))
        url_ = params["url"][0]
        xbmc.Player().play(url_)

        channel_code = params["channel_code"][0]
        playlist_for_channel = get_playlist_for_channel(channel_code)
        songs = playlist_for_channel.songs

        play_list = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
        play_list.clear()
        play_list.unshuffle()
        if len(songs) > 0:
            for i, song in enumerate(songs):
                # xbmc.log("Adding playlist item: %s" % song)
                play_list.add(url=create_qs({
                    'url': url_,
                    'channel_code': channel_code
                }), listitem=xbmcgui.ListItem(label="%s - %s" % (song.artist, song.title),
                                              label2=song.artist,
                                              iconImage=song.image_url,
                                              thumbnailImage=song.image_url))
