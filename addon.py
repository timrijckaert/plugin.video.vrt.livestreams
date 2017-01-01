import sys
import urlparse
import xbmcgui
import xbmcplugin
from resources.lib.utils.debugger import start_debugger
from resources.lib.utils.radiochannel import get_all_radio_channels
from resources.lib.utils.videochannel import get_all_video_channels

self = sys.argv[0]
handle = int(sys.argv[1])
qs = sys.argv[2]

__in_debug__ = False

if __in_debug__:
    start_debugger()


def get_radio_list_items():
    radio_items = []
    for channel in get_all_radio_channels():
        live_stream_title = channel.title
        live_stream_url = channel.url
        list_item = xbmcgui.ListItem(label=live_stream_title,
                                     iconImage=channel.picture,
                                     thumbnailImage=channel.picture,
                                     path=live_stream_url)
        list_item.setInfo(type='audio', infoLabels={"title": live_stream_title, "tagline": channel.description})
        list_item.setProperty("isPlayable", 'true')
        radio_items.append((live_stream_url, list_item))
    return radio_items


def get_video_list_items():
    video_items = []
    for channel in get_all_video_channels():
        live_stream_title = channel.title
        live_stream_url = channel.video_url
        list_item = xbmcgui.ListItem(label=live_stream_title,
                                     iconImage=channel.picture,
                                     thumbnailImage=channel.picture,
                                     path=live_stream_url)
        list_item.setInfo(type='video', infoLabels={"title": live_stream_title})
        list_item.setProperty("isPlayable", 'true')
        video_items.append((live_stream_url, list_item))
    return video_items


def display_generic_playable_items(items):
    xbmcplugin.addDirectoryItems(handle=handle, items=items, totalItems=len(items))
    xbmcplugin.endOfDirectory(handle, True)


if len(qs) > 1:
    params = urlparse.parse_qs(qs[1:])
    if params["content_type"][0] == "video":
        display_generic_playable_items(get_video_list_items())
    else:
        display_generic_playable_items(get_radio_list_items())
