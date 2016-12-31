import xbmcaddon, xbmcgui
from resources.lib.utils.debugger import startdebugger

debug = True
if debug:
    startdebugger()

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "Hello World Tim!"
line2 = "We can write anything we want here"
line3 = "Using Python"

xbmcgui.Dialog().ok(addonname, line1, line2, line3)