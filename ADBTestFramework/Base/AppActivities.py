import subprocess
class sravan:

    def isDeviceConnected(self):
        """
        ==========================================================
        This Method is to Check Weather Device is Connected or not
        ==========================================================
        """
        count=0
        try:
            subprocess.Popen("adb start-server ", stdout=subprocess.PIPE, shell=True)
            asd = subprocess.Popen("adb devices ", stdout=subprocess.PIPE, shell=True)
            (output, err) = asd.communicate()
            asd.wait()
            for device in ((str(output.decode('ascii'))).splitlines()):
                    count+=1
            if count == 2:
                return False
            else:
                return True
        except(RuntimeError, subprocess.SubprocessError)as e:
            print(str(e.message))


    def isAppInDevice(self,packageName):
        """
        ==============================================
        This Method is to Check wather
        Application is Present in the Device Connected
        using  package log file
         ==============================================
         """
        try:
            asd=subprocess.Popen("adb shell pm list packages ", stdout=subprocess.PIPE, shell=True)
            (output, err) = asd.communicate()
            asd.wait()
            for line in ((str(output.decode('ascii'))).splitlines()):
                if packageName in line:
                    return True
            else:
                return False
        except(RuntimeError, subprocess.SubprocessError)as e:
            print(str(e.message))

    def launchApp(self,packageName):


        """
                ======================================================
                This Method is to Launch the Application
                                and
                Check weather Application launched successfully or not
                by using recent activity log file
                ======================================================
        """

        try:
            subprocess.Popen("adb shell monkey -p " + packageName + " -c " + "android.intent.category.LAUNCHER 1", stdout=subprocess.PIPE, shell=True)
            asd = subprocess.Popen("adb shell dumpsys activity recents  ", stdout=subprocess.PIPE, shell=True)
            (output, err) = asd.communicate()
            asd.wait()
            for line in ((str(output.decode('ascii'))).splitlines()):
                if packageName in line:
                    return True
            else:
                return False
        except(RuntimeError, subprocess.SubprocessError)as e:
                print(str(e.message))



