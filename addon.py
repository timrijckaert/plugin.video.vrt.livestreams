import xbmc
import xbmcaddon
import xbmcgui
from resources.lib.utils.debugger import start_debugger

start_debugger()

if __name__ == '__main__':
    addon = xbmcaddon.Addon('plugin.video.kodiplayground')
    icon = addon.getAddonInfo('icon')
    link = "http://live.stream.vrt.be/vrt_stubru_live/stream1296/playlist.m3u8"
    title = "Studio Brussel Live Stream"
    list_item = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon, path=link)
    list_item.setInfo(type='Video', infoLabels={"Title": title})
    list_item.setProperty("isPlayable", 'true')

    player = xbmc.Player()
    player.play(item=link, listitem=list_item)
