import xbmcaddon

PLUGIN_NAME = xbmcaddon.Addon('plugin.video.vrt.livestreams').getAddonInfo("name")

ACTIONS = {
    "radio_list_item_clicked": "radio_list_item_clicked_action"
}
