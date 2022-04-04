#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time

class ultrasonic:

    def __init__(self,trig,echo):
        self.TRIG=trig
        self.ECHO=echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(echo, GPIO.IN)
        GPIO.setup(trig, GPIO.OUT)


    def get_distance(self):
        send_time = 0
        rece_time = 0
        GPIO.output( self.TRIG, GPIO.LOW)
        time.sleep(0.002)
        GPIO.output( self.TRIG, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output( self.TRIG, GPIO.LOW)
        while GPIO.input(self.ECHO) == 0:
            send_time = time.time()
            pass
        while GPIO.input(self.ECHO) == 1:
            rece_time = time.time()
            pass
        distance = (rece_time - send_time) * 340 / 2 * 100
        return distance

