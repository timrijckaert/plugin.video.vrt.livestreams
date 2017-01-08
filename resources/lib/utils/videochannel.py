class VideoChannel(object):
    def __init__(self, title, thumbnail_picture, fanart_picture, video_url):
        self.title = title
        self.thumbnail_picture = thumbnail_picture
        self.fanart_picture = fanart_picture
        self.video_url = video_url


journaal = VideoChannel("Journaal",
                        "http://images.vrt.be/orig/2016/05/29/8b20f674-2585-11e6-8682-00163edf843f.png",
                        "http://images.vrt.be/orig/2016/08/22/71b84de4-6838-11e6-94b1-00163edf843f.jpg",
                        "http://live.stream.vrt.be/vrt_journaal_live/stream1296/playlist.m3u8")

een = VideoChannel("Een",
                   "https://cache02.ps.yelo.prd.telenet-ops.be/yposter/images/channellogos/sqlogo_MM24E.png",
                   "http://images.vrt.be/orig/2016/08/22/2a6dc40b-6839-11e6-94b1-00163edf843f.jpg",
                   "http://live.stream.vrt.be/vrt_video1_live/smil:vrt_video1_live.smil/playlist.m3u8")

canvas = VideoChannel("Canvas",
                      "https://cache03.ps.yelo.prd.telenet-ops.be/yposter/images/channellogos/sqlogo_MM24F.png",
                      "http://images.vrt.be/orig/2016/04/18/5a4d2de0-0562-11e6-8682-00163edf843f.jpg",
                      "http://live.stream.vrt.be/vrt_video2_live/smil:vrt_video2_live.smil/playlist.m3u8")

ketnet = VideoChannel("Ketnet",
                      "http://images.vrt.be/orig/2016/05/29/419b3f11-2585-11e6-8682-00163edf843f.png",
                      "http://images.vrt.be/orig/2016/04/29/12c63a9e-0e12-11e6-8682-00163edf843f.jpg",
                      "http://live.stream.vrt.be/vrt_events3_live/smil:vrt_events3_live.smil/playlist.m3u8")

studio_brussel = VideoChannel("Studio Brussel Livestream",
                              "http://images.vrt.be/orig/2016/05/27/65b13069-2430-11e6-8682-00163edf843f.png",
                              "http://images.vrt.be/orig/2016/08/29/dfec2c7e-6df9-11e6-94b1-00163edf843f.jpg",
                              "http://live.stream.vrt.be/vrt_stubru_live/smil:vrt_stubru_live.smil/playlist.m3u8")

mnm = VideoChannel("MNM Livestream",
                   "http://images.vrt.be/orig/2016/05/27/8004d7fb-2430-11e6-8682-00163edf843f.png",
                   "http://images.vrt.be/orig/2014/08/11/06a3acc6-2169-11e4-b923-00163edf75b7.png",
                   "http://live.stream.vrt.be/vrt_mnm_live/stream1296/playlist.m3u8")


def get_all_video_channels():
    return [
        journaal,
        een,
        canvas,
        ketnet,
        studio_brussel,
        mnm
    ]
