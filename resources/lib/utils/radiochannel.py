class RadioChannel(object):
    def __init__(self, channel_code, title, description, picture, url):
        self.channel_code = channel_code
        self.title = title
        self.description = description
        self.picture = picture
        self.url = url


radio_1 = RadioChannel("11",
                       "Radio 1",
                       "Altijd benieuwd",
                       "http://images.vrt.be/orig/2016/05/27/e4f31ec0-242f-11e6-8682-00163edf843f.png",
                       "http://mp3.streampower.be/radio1.aac")

radio_2 = RadioChannel("24",
                       "Radio 2",
                       "De grootste familie",
                       "http://images.vrt.be/orig/2016/05/27/283dfce2-2430-11e6-8682-00163edf843f.png",
                       "http://mp3.streampower.be/ra2ovl.aac")

klara = RadioChannel("31",
                     "Klara",
                     "Blijf verwonderd",
                     "http://images.vrt.be/orig/2016/05/27/4b635533-2430-11e6-8682-00163edf843f.png",
                     "http://mp3.streampower.be/klara.aac")

klara_continuo = RadioChannel("32",
                              "Klara Continuo",
                              "Blijf verwonderd",
                              "http://images.vrt.be/orig/2016/05/29/5ea8af72-2585-11e6-8682-00163edf843f.png",
                              "http://mp3.streampower.be/klaracontinuo.aac")

studio_brussel = RadioChannel("41",
                              "Studio Brussel",
                              "Life is music",
                              "http://images.vrt.be/orig/2016/05/27/65b13069-2430-11e6-8682-00163edf843f.png",
                              "http://mp3.streampower.be/stubru.aac")

mnm = RadioChannel("55",
                   "MNM",
                   "Music & More",
                   "http://images.vrt.be/orig/2016/05/27/8004d7fb-2430-11e6-8682-00163edf843f.png",
                   "http://mp3.streampower.be/mnm.aac")

mnm_hits = RadioChannel("56",
                        "MNM Hits",
                        "Music & More",
                        "http://images.vrt.be/orig/2016/05/29/757af873-2585-11e6-8682-00163edf843f.png",
                        "http://mp3.streampower.be/mnm_hits.aac")

ketnet_hits = RadioChannel("03",
                           "Ketnet Hits",
                           "",
                           "http://images.vrt.be/orig/2016/05/29/419b3f11-2585-11e6-8682-00163edf843f.png",
                           "http://mp3.streampower.be/ketnetradio.aac")

vrtnieuws = RadioChannel("13",
                         "VRT Nieuws",
                         "",
                         "http://images.vrt.be/orig/2016/05/29/8b20f674-2585-11e6-8682-00163edf843f.png",
                         "http://download.stream.vrt.be/apps/services_sac/published/web/fixed/11_11niws-snip_hi.mp3")


def get_all_radio_channels():
    return [
        radio_1,
        radio_2,
        klara,
        klara_continuo,
        studio_brussel,
        mnm,
        mnm_hits,
        ketnet_hits,
        vrtnieuws
    ]
