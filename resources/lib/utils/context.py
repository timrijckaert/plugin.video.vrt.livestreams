import os

import xbmcaddon

__addon__ = xbmcaddon.Addon()
__img_dir__ = os.path.join(__addon__.getAddonInfo("path"), "resources", "media")


def get_icon(icon_name):
    resolved_img_path = "%s_icon.png" % (icon_name.lower())
    return os.path.join(__img_dir__, resolved_img_path)
