#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(format='%(asctime)s  - %(levelname)s:%(message)s', level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)
class Ultrasonic:

    def __init__(self, trig, echo):
        self.TRIG = trig
        self.ECHO = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(echo, GPIO.IN)
        GPIO.setup(trig, GPIO.OUT)
        logging.info("超声波检测模块初始化完成")

    def __destroy__(self):
        GPIO.cleanup(self.ECHO)
        GPIO.cleanup(self.TRIG)
        logging.info("超声波输出端口已复位")

    def get_distance(self):
        send_time = 0
        rece_time = 0
        GPIO.output(self.TRIG, GPIO.LOW)
        time.sleep(0.002)
        GPIO.output(self.TRIG, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(self.TRIG, GPIO.LOW)
        while GPIO.input(self.ECHO) == 0:
            send_time = time.time()
            pass
        while GPIO.input(self.ECHO) == 1:
            rece_time = time.time()
            pass
        distance = (rece_time - send_time) * 340 / 2 * 100
        return distance


# def test():
#     test = Ultrasonic(17,27)
#     logging.info(test.get_distance())
#     pass
# test()
