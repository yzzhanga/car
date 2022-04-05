#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time

from orderSetv2 import L298nOrder
from communication import mqutils
import threading
import ultrasonic
#加载指令集
order =L298nOrder([26,19],[13,10],[21,20], [16,12])
redis =mqutils(host='mq.yzzhanga.xyz', port= 46379, password= '1qaz2wsx', db= 0)


class OrderThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        redis.connection()
        print("指令接收线程初始化完成")

    def run(self):
        print("指令接收线程开始运行")
        redis.receive("car_order_queue", order)

class UltrasonicThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sonic = ultrasonic(17,27)
    def run(self):
        while True:
            dis = self.sonic.get_distance()
            if (dis<0.1):
                order.setting()
            time.sleep(1)

orderThread = OrderThread()
orderThread.start()

ultrasonicThread = UltrasonicThread()
ultrasonicThread.start()

