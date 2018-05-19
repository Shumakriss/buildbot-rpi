#!/usr/bin/python

import queue
import threading
import time
#import redis


def kinesis_command_consumer(target_queue):
    print("Thread called")
    while True:
        target_queue.put("command")
        time.sleep(1)


def handle_command(command):
    print(command)


def capture_video_frame(target_queue):
    return "frame"


def kinesis_video_producer(target_queue):
    return "frame"


def capture_sensor_data(target_queue):
    return "sensor data"


def kinesis_data_producer(target_queue):
    return "data"


class BuildBotRpi:

    def __init__(self):
        self.shutdown = False
        self.threads = []

    def stop(self):
        self.shutdown = True
        for thread in self.threads:
            thread.join()

    def start(self):
        print("Running")

        command_queue = queue.PriorityQueue()
        video_queue = queue.Queue()
        sensor_queue = queue.Queue()

        self.threads = {
            threading.Thread(target=kinesis_command_consumer, args=(command_queue,)),
            threading.Thread(target=kinesis_video_producer, args=(video_queue,)),
            threading.Thread(target=kinesis_data_producer, args=(sensor_queue,)),
            threading.Thread(target=capture_video_frame, args=(video_queue,)),
            threading.Thread(target=capture_sensor_data, args=(sensor_queue,))
        }

        for thread in self.threads:
            thread.start()

        while not self.shutdown:
            try:
                cmd = command_queue.get(block=False)
                handle_command(cmd)
            except queue.Empty:
                time.sleep(1)


if __name__ == '__main__':
    daemon = BuildBotRpi()
    daemon.start()
