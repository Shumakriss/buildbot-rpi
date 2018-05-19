#!/usr/bin/python
import unittest
from buildbot import daemon
import signal


class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


class MyTest(unittest.TestCase):
    def test(self):
        test_daemon = daemon.BuildBotRpi()
        try:
            with timeout(seconds=5):
                test_daemon.start()
        except TimeoutError:
            pass
        test_daemon.stop()


if __name__ == '__main__':
    unittest.main()