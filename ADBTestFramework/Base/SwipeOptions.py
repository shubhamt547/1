import subprocess


class swipe:

        # Scroll a little from bottom
    def vertical_scrollUp_little(self):
        p = subprocess.Popen("adb shell input swipe 520 1750 520 1300", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        # Swipe from bottom to top
    def vertical_scrollUp_fullscreen(self):
        p = subprocess.Popen("adb shell input swipe 520 1500 520 200", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        # Swipe from top to bottom (Excluding Notification Bar)
    def vertical_scrollDown_fullscreen(self):
        p = subprocess.Popen("adb shell input swipe 520 200 520 1500", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        # Scroll Horizontally from Left to Right
    def vertical_swipe_right(self):
        p = subprocess.Popen("adb shell input swipe 300 1000 2000 1000", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        # Scroll Horizontally from Right to Left
    def vertical_swipe_left(self):
        p = subprocess.Popen("adb shell input swipe 1000 800 -50 800", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()