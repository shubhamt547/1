import os
import subprocess
from builtins import str
from builtins import print

class DeviceProps:

    # ---------------------This function is used to find device properties-------------------------------------
    def find_device_properties(self, propertyName):
        try:
            p = subprocess.Popen("adb shell getprop " + propertyName, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p.wait()
            print(
                str(output.decode('ascii')))
            print()
            return str(output.decode('ascii'))
        except (RuntimeError, subprocess.SubprocessError) as e:
            print(str(e.message))
            raise