import queue
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildbot import daemon


class MyTest(unittest.TestCase):
    def test(self):
        test_queue = queue.Queue()
        self.assertEqual(daemon.capture_video_frame(test_queue), "frame")


if __name__ == '__main__':
    unittest.main()