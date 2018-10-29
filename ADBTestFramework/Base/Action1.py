import time
import subprocess
from Base.RepositoryFiles import Respository

class appinstalluninstall:
    def install(self, appPath):
        try:
            asd=subprocess.Popen("adb install -r "+ appPath,stdout=subprocess.PIPE,shell=True)
            output,err=asd.communicate()
            asd.wait()
        except(RuntimeError,subprocess.SubprocessError) as e:
            print(str(e.message))

    def uninstall(self):
        try:
            packname=input("enter package name to uninstall:")
            subprocess.Popen("adb shell pm uninstall -k " +packname,stdout=subprocess.PIPE,shell=True)
        except(RuntimeError,subprocess.SubprocessError) as e:
            print (str(e.message))


# obj=appinstalluninstall()
# obj.install(Respository.facebookApp)
# time.sleep(5)
# obj.uninstall()
