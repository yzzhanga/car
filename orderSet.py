#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep
import RPi.GPIO as GPIO

# POINT = [5,6,16,26]
LEFT_FRONT_FPORT = [26,17]
LEFT_BACK_FPORT = [27,22]
RIGHT_FRONT_PORT = [18,23]
RIGHT_BACK_PORT = [24,25]

GPIO.setwarnings(False)

class L298nOrder:
    
    def setup():
        print("指令集初始化成功")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LEFT_FRONT_FPORT,GPIO.OUT)
        GPIO.setup(LEFT_BACK_FPORT,GPIO.OUT)
        GPIO.setup(RIGHT_FRONT_PORT,GPIO.OUT)
        GPIO.setup(RIGHT_BACK_PORT,GPIO.OUT)

    def turnLeftRound(leftBool):
        if (leftBool):
            GPIO.output(LEFT_FRONT_FPORT[0],True)
            GPIO.output(LEFT_FRONT_FPORT[1],False)
            GPIO.output(RIGHT_BACK_PORT[0],False)
            GPIO.output(RIGHT_BACK_PORT[1],True)
            print ("执行指令:左转向")
        else:
            GPIO.output(LEFT_FRONT_FPORT[0],False)
            GPIO.output(LEFT_FRONT_FPORT[1],True)
            GPIO.output(RIGHT_BACK_PORT[0],True)
            GPIO.output(RIGHT_BACK_PORT[1],False)
            print ("执行指令:左转倒车")

    def turnRightRound(rightBool):
        if (rightBool):
            GPIO.output(RIGHT_FRONT_PORT[0],True)
            GPIO.output(RIGHT_FRONT_PORT[1],False)
            GPIO.output(LEFT_BACK_FPORT[0],False)
            GPIO.output(LEFT_BACK_FPORT[1],True)
            print ("执行指令:右转向")
        else:
            GPIO.output(RIGHT_FRONT_PORT[0],False)
            GPIO.output(RIGHT_FRONT_PORT[1],True)
            GPIO.output(LEFT_BACK_FPORT[0],True)
            GPIO.output(LEFT_BACK_FPORT[1],False)
            print ("执行指令:右转倒车")

    def allMove():
        GPIO.output(LEFT_FRONT_FPORT[0],True)
        GPIO.output(LEFT_FRONT_FPORT[1],False)
        GPIO.output(LEFT_BACK_FPORT[0],True)
        GPIO.output(LEFT_BACK_FPORT[1],False)
        GPIO.output(RIGHT_FRONT_PORT[0],True)
        GPIO.output(RIGHT_FRONT_PORT[1],False)
        GPIO.output(RIGHT_BACK_PORT[0],True)
        GPIO.output(RIGHT_BACK_PORT[1],False)
        print ("执行指令:前进")

    def allBack():
        GPIO.output(LEFT_FRONT_FPORT[0],False)
        GPIO.output(LEFT_FRONT_FPORT[1],True)
        GPIO.output(LEFT_BACK_FPORT[0],False)
        GPIO.output(LEFT_BACK_FPORT[1],True)
        GPIO.output(RIGHT_FRONT_PORT[0],False)
        GPIO.output(RIGHT_FRONT_PORT[1],True)
        GPIO.output(RIGHT_BACK_PORT[0],False)
        GPIO.output(RIGHT_BACK_PORT[1],True)
        print ("执行指令:后退")

    def stop():
        GPIO.output(LEFT_FRONT_FPORT[0],False)
        GPIO.output(LEFT_FRONT_FPORT[1],False)
        GPIO.output(LEFT_BACK_FPORT[0],False)
        GPIO.output(LEFT_BACK_FPORT[1],False)
        GPIO.output(RIGHT_FRONT_PORT[0],False)
        GPIO.output(RIGHT_FRONT_PORT[1],False)
        GPIO.output(RIGHT_BACK_PORT[0],False)
        GPIO.output(RIGHT_BACK_PORT[1],False)
        print ("执行指令:停止")

