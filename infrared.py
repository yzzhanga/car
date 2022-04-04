#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO

class infrared:

    def __init__(self,detectors=[]):
        self.DETECTORS=detectors
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(detectors, GPIO.IN)

    def detect(self,index):
         selector = self.DETECTORS[index]
         return GPIO.input(selector) == GPIO.LOW
