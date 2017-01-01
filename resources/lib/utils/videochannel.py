class VideoChannel(object):
    def __init__(self, title, picture, video_url):
        self.title = title
        self.picture = picture
        self.video_url = video_url


journaal = VideoChannel("Journaal",
                        "http://images.vrt.be/orig/2016/05/29/8b20f674-2585-11e6-8682-00163edf843f.png",
                        "http://live.stream.vrt.be/vrt_journaal_live/stream1296/playlist.m3u8")

een = VideoChannel("Een",
                   "https://cache02.ps.yelo.prd.telenet-ops.be/yposter/images/channellogos/sqlogo_MM24E.png",
                   "http://live.stream.vrt.be/vrt_video1_live/smil:vrt_video1_live.smil/playlist.m3u8")

canvas = VideoChannel("Canvas",
                      "https://cache03.ps.yelo.prd.telenet-ops.be/yposter/images/channellogos/sqlogo_MM24F.png",
                      "http://live.stream.vrt.be/vrt_video2_live/smil:vrt_video2_live.smil/playlist.m3u8")

ketnet = VideoChannel("Ketnet",
                      "http://images.vrt.be/orig/2016/05/29/419b3f11-2585-11e6-8682-00163edf843f.png",
                      "http://live.stream.vrt.be/vrt_events3_live/smil:vrt_events3_live.smil/playlist.m3u8")


def get_all_video_channels():
    return [
        journaal,
        een,
        canvas,
        ketnet
    ]
