import unittest
import filecomp


class MyTestCase(unittest.TestCase):
    def test_empty_folder(self):
        self.assertEqual(filecomp.fcomp("D:/test_folder_empty"), None)

    def test_regular_1(self):
        self.assertEqual(filecomp.fcomp("D:/test_folder")["maxs"][0], "D:/test_folder/expected")

    def test_regular_2(self):
        self.assertEqual(filecomp.fcomp("D:\\test_folder")["mins"][0], "D:/test_folder/загружено.htm")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(filecomp.fcomp("D:\test_folder")["maxs"][0], "D:/test_folder/expected")


if __name__ == '__main__':
    unittest.main()
