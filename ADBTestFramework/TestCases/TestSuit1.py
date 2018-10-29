from Base.FileOperations import FileOperation as fo
from Base.RepositoryFiles import Respository as rep
import unittest
class TestSuit1(unittest.TestCase):


    def test_TestCase1(self):
        fo.write_data_file(rep, rep.filePath + rep.txtFile, fo.get_file_of_particular_type(fo, rep.music_Folder, rep.mp3))

    def test_TestCase2(self):

if __name__ == '__main__':
    unittest.main()