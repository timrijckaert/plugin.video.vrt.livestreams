import sys
import xbmc
import xbmcgui
import xbmcplugin
from resources.lib.models.constants import ACTIONS
from resources.lib.models.radiochannel import get_all_radio_channels
from resources.lib.models.videochannel import get_all_video_channels
from resources.lib.service.playlistfetcher import get_playlist_for_channel
from resources.lib.utils.debugger import Debugger
from resources.lib.utils.utils import Utils

self = sys.argv[0]
addon_handle = int(sys.argv[1])
qs = sys.argv[2]


def get_radio_list_items():
    radio_items = []
    for channel in get_all_radio_channels():
        live_stream_title = channel.title
        live_stream_url = utils.create_qs(self, {
            'action': ACTIONS["radio_list_item_clicked"],
            'url': channel.url,
            'channel_code': channel.channel_code
        })

        list_item = xbmcgui.ListItem(label=live_stream_title,
                                     label2=channel.description,
                                     iconImage=channel.thumbnail_picture,
                                     thumbnailImage=channel.thumbnail_picture,
                                     path=live_stream_url)
        list_item.setProperty("fanart_image", channel.fanart_picture)
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
    xbmcplugin.addDirectoryItems(handle=addon_handle, items=items, totalItems=len(items))
    xbmcplugin.endOfDirectory(addon_handle, True)


if __name__ == "__main__":
    utils = Utils()
    debugger = Debugger()

if len(qs) > 1:
    action = utils.get_action(qs)
    xbmc.log("Action %s" % action)

    if action is None:
        if utils.content_type == 'video':
            display_generic_playable_items(get_video_list_items())
        else:
            display_generic_playable_items(get_radio_list_items())

    if action == ACTIONS["radio_list_item_clicked"]:
        xbmc.Player().play(utils.url)
        playlist_for_channel = get_playlist_for_channel(utils.channel_code)
        songs = playlist_for_channel.songs

        play_list = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
        play_list.clear()
        play_list.unshuffle()
        if len(songs) > 0:
            for song in songs:
                play_list.add(url=utils.construct_known_params(self),
                              listitem=xbmcgui.ListItem(label="%s - %s" % (song.artist, song.title),
                                                        label2=song.artist,
                                                        iconImage=song.image_url,
                                                        thumbnailImage=song.image_url))
