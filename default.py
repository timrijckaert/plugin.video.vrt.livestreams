import xbmc, xbmcgui


# name and crete our window
class BlahMainWindow(xbmcgui.Window):
    # and define it as self
    def __init__(self):
        # add picture control to our window (self) with a hardcoded path name to picture
        self.addControl(xbmcgui.ControlImage(0, 0, 720, 480, "Q:\\scripts\\background.jpg"))

# store our window as a short variable for easy of use
W = BlahMainWindow()
# run our window we created with our background jpeg image
W.doModal()
# After the window is closed, Destroy it
del W