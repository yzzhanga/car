#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time

from orderSetv2 import L298nOrder
from communication import mqutils
import threading
from ultrasonic import Ultrasonic
import logging

logging.basicConfig(format='%(asctime)s  - %(levelname)s:%(message)s', level=logging.DEBUG)
logging.getLogger().setLevel(logging.INFO)
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# 加载指令集
order = L298nOrder([26, 19], [13, 10], [21, 20], [16, 12])
redis = mqutils(host='mq.yzzhanga.xyz', port=46379, password='1qaz2wsx', db=0)

class OrderThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        redis.connection()
        logging.info("指令接收线程初始化完成")

    def run(self):
        logging.info("指令接收线程开始运行")
        redis.receive("car_order_queue", order)


class UltrasonicThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sonic = Ultrasonic(17, 27)
        while True:
            dis = sonic.get_distance()
            if (dis < 2):
                order.setting()
            time.sleep(1)

def main():
    # class infraredThread(threading.Thread)

    orderThread = OrderThread()
    orderThread.start()

    ultrasonicThread = UltrasonicThread()
    ultrasonicThread.start()

if __name__ == '__main__':
    main()
