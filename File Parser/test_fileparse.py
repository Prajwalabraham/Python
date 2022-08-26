import filecmp
from fileparse import Fileparse
import unittest
from unittest.mock import patch, call
import io

class TestFileParser(unittest.TestCase):

    def test_fileparser(self):
        Fileparse("logfile.txt")
        self.assertFalse(filecmp.cmp("Info.txt", "test_Info.txt", shallow=False))

if __name__=="__main__":
    unittest.main()
