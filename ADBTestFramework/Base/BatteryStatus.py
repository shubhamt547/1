import  subprocess
class Battery:
    def batterystatus(self,state):
        try:
            adb=subprocess.Popen("adb shell dumpsys battery",stdout=subprocess.PIPE,shell=True)
            output,err=adb.communicate()
            b=(output.decode())
            fp=str(b).split()
            adb.wait()
            for line in range(0,len(fp)):
                if state in fp[line]:
                    return str((fp[line+1]))

        except(RuntimeError, subprocess.subprocesserror) as e:
            print(str(e.message))









































