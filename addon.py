import sys
import urllib
import urlparse

import xbmc
import xbmcgui
import xbmcplugin
from resources.lib.utils.channelprovider import get_root_channels
from resources.lib.utils.context import get_icon

self = sys.argv[0]
handle = int(sys.argv[1])
qs = sys.argv[2]

if len(qs) > 1:
    params = urlparse.parse_qs(qs[1:])
    xbmc.log(str(params))

for key in get_root_channels().keys():
    icon = get_icon(key)
    root_li = xbmcgui.ListItem(label=key)
    url = self + '?' + urllib.urlencode({'url': key.lower()})
    root_li.setInfo('video', {'title': key})
    xbmcplugin.addDirectoryItem(handle, url, root_li, True)
# for channel in get_all_video_channels():
#     live_stream_title = channel.title
#     live_stream_url = channel.video_url
#     list_item = xbmcgui.ListItem(label=live_stream_title,
#                                  iconImage=channel.picture,
#                                  thumbnailImage=channel.picture,
#                                  path=live_stream_url)
#     list_item.setInfo(type='Video', infoLabels={"Title": live_stream_title})
#     list_item.setProperty("isPlayable", 'true')
#     xbmcplugin.addDirectoryItem(handle, live_stream_url, list_item, isFolder=False)

xbmcplugin.endOfDirectory(handle, True)
