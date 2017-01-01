from resources.lib.utils.radiochannel import get_all_radio_channels
from resources.lib.utils.videochannel import get_all_video_channels


def get_root_channels():
    radio_channels = get_all_radio_channels()
    video_channel = get_all_video_channels()
    return {"TV": video_channel, "RADIO": radio_channels}
