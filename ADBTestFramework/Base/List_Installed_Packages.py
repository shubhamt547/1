import subprocess
from builtins import print,str

class Packages:
    def listpackages(self, packageName):
        """Method returns the list of all the packages in the device"""
        try:
            l = subprocess.Popen("adb shell pm list packages | grep " + packageName, stdout=subprocess.PIPE, shell=True)
            (output, err) = l.communicate()
            l.wait()
            print(str(output.decode('ascii')))
            return (str(output.decode('ascii')))
        except(RuntimeError, subprocess.SubprocessError)as e:
            print(str(e.message))