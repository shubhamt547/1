import subprocess
from builtins import str
from builtins import print


class FileOperation:

    def search_folder(self):
        try:
            p = subprocess.Popen("adb shell ls /sdcard/", stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p.wait()
            print(str(output.decode('ascii')))
            print()
            return str(output.decode('ascii'))
        except (RuntimeError, subprocess.SubprocessError) as e:
            print(str(e.message))
            raise

    def finding_folder_in_SDCARD(FileOperation, folderName):
        try:
            finding_folder = FileOperation.search_folder()
            if folderName in finding_folder:
                print(folderName + " : Found")
                return True
            else:
                print(folderName + "NotFound")
                return False
        except (RuntimeError, subprocess.SubprocessError) as e:
            print(str(e.message))
            raise

    def get_All_FilesIn_Folder(self, folderName):
        try:
            ifFolder_Found = self.finding_folder_in_SDCARD(folderName)
            if ifFolder_Found == True:
                p = subprocess.Popen("adb shell ls /sdcard/" + folderName, stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                p.wait()
                print(str(output.decode('ascii')))
                print()
        except (RuntimeError, subprocess.SubprocessError) as e:
            print(str(e.message))
            raise
        return str(output.decode('ascii'))

    def get_file_of_particular_type(FileOperation, folderName, fileFormat):
        try:
            ifFolder_Found = FileOperation.finding_folder_in_SDCARD(FileOperation,folderName)
            if ifFolder_Found == True:
                p = subprocess.Popen("adb shell ls /sdcard/" + folderName + "/*" + fileFormat, stdout=subprocess.PIPE,
                                     shell=True)
                (output, err) = p.communicate()
                p.wait()
                print(str(output.decode('ascii')))
                print()
        except (RuntimeError, subprocess.SubprocessError) as e:
            print(str(e.message))
            raise
        return str(output.decode('ascii'))

    def number_of_filesAndFolder(self):
        full_list = self.search_folder()
        number_of_files = len(full_list)
        print(" Number of files :: " + str(number_of_files))


    def write_data_file(fullPath, anyText):
        f = open(fullPath, "w+")
        f.write(anyText)
        f.close()