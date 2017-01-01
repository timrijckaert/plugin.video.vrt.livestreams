class Channel(object):
    def __init__(self, title, picture, video_url, is_radio_channel=True):
        self.title = title
        self.picture = picture
        self.video_url = video_url
        self.is_radio_channel = is_radio_channel


studio_brussel = Channel("Studio Brussel",
                         "http://radioplus.be/img/channels/stubru/logo.png",
                         "http://live.stream.vrt.be/vrt_stubru_live/stream1296/playlist.m3u8")

radio_2 = Channel("Radio 2",
                  "http://radioplus.be/img/channels/radio2/logo.png",
                  "http://live.stream.vrt.be/vrt_events2_live/smil:vrt_events2_live.smil/playlist.m3u8")

ketnet = Channel("Ketnet",
                 "https://www.ketnet.be/sites/all/themes/ketnet/logo.png",
                 "http://live.stream.vrt.be/vrt_events3_live/smil:vrt_events3_live.smil/playlist.m3u8")

journaal = Channel("Journaal",
                   "http://deredactie.be/polopoly_fs/1.2614381!image/1912478174.png",
                   "http://live.stream.vrt.be/vrt_journaal_live/stream1296/playlist.m3u8",
                   False)

mnm = Channel("MNM",
              "http://radioplus.be/img/channels/mnm/logo.png",
              "http://live.stream.vrt.be/vrt_mnm_live/smil:vrt_mnm_live.smil/playlist.m3u8")

een = Channel("Een",
              "https://www.vrt.be/etc/designs/corporate/clientlib-site/assets/images/brands/logo/een_v2.svg",
              "http://live.stream.vrt.be/vrt_video1_live/smil:vrt_video1_live.smil/playlist.m3u8",
              False)

canvas = Channel("Canvas",
                 "https://www.vrt.be/etc/designs/corporate/clientlib-site/assets/images/brands/logo/canvas--green.svg",
                 "http://live.stream.vrt.be/vrt_video2_live/smil:vrt_video2_live.smil/playlist.m3u8",
                 False)
channels = [
    studio_brussel,
    radio_2,
    mnm,
    journaal,
    een,
    canvas,
    ketnet
]


def get_all_radio_channels():
    return [c for c in channels if c.is_radio_channel]


def get_all_channels():
    return channels
