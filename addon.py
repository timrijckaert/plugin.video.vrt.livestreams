import sys

import xbmcaddon
import xbmcgui
import xbmcplugin
from resources.lib.utils.channelprovider import get_root_channels
from resources.lib.utils.debugger import start_debugger
from resources.lib.utils.videochannel import get_all_video_channels

start_debugger()

__addon__ = xbmcaddon.Addon()

self = sys.argv[0]
handle = int(sys.argv[1])
qs = sys.argv[2]

if __name__ == '__main__':
    root_channel = get_root_channels()
    for channel in get_all_video_channels():
        live_stream_title = channel.title
        live_stream_url = channel.video_url
        list_item = xbmcgui.ListItem(label=live_stream_title,
                                     iconImage=channel.picture,
                                     thumbnailImage=channel.picture,
                                     path=live_stream_url)
        list_item.setInfo(type='Video', infoLabels={"Title": live_stream_title})
        list_item.setProperty("isPlayable", 'true')
        xbmcplugin.addDirectoryItem(handle, live_stream_url, list_item, isFolder=False)

xbmcplugin.endOfDirectory(handle, True)
