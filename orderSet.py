#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep
import RPi.GPIO as GPIO

# POINT = [5,6,16,26]
# GPIO接口结合
LEFT_FRONT_PORT = [10,17] #左前轮 正负输出，这两个输出互斥，不能同时为正，但可以同时为负，不管同时为正或负，都视为刹车；
LEFT_BACK_PORT = [27,22] #左后轮
RIGHT_FRONT_PORT = [18,23] #右前轮
RIGHT_BACK_PORT = [24,25] #右后轮

#忽略重复setmode导致的报警，一般是在关闭程序时候没有调用destory方法导致
GPIO.setwarnings(False)

class L298nOrder:
    
    def setup():
        print("指令集初始化成功")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LEFT_FRONT_PORT,GPIO.OUT)
        GPIO.setup(LEFT_BACK_PORT,GPIO.OUT)
        GPIO.setup(RIGHT_FRONT_PORT,GPIO.OUT)
        GPIO.setup(RIGHT_BACK_PORT,GPIO.OUT)

    #关闭GPIO的输出设置（这里有个前提是GPIO全部服务本集合，右可能会误关闭其他GPIO组合程序）
    def destory():
        print("指令驱动销毁")
        GPIO.cleanup()

    #转向程序 左中心线的顺时针和逆时针旋转
    def turnLeftRound(leftBool):
        if (leftBool):
            GPIO.output(LEFT_FRONT_PORT[0],True)
            GPIO.output(LEFT_FRONT_PORT[1],False)
            GPIO.output(RIGHT_BACK_PORT[0],False)
            GPIO.output(RIGHT_BACK_PORT[1],True)
            print ("执行指令:左转向")
        else:
            GPIO.output(LEFT_FRONT_PORT[0],False)
            GPIO.output(LEFT_FRONT_PORT[1],True)
            GPIO.output(RIGHT_BACK_PORT[0],True)
            GPIO.output(RIGHT_BACK_PORT[1],False)
            print ("执行指令:左转倒车")
    #转向程序 右中心线的顺时针和逆时针旋转
    def turnRightRound(rightBool):
        if (rightBool):
            GPIO.output(RIGHT_FRONT_PORT[0],True)
            GPIO.output(RIGHT_FRONT_PORT[1],False)
            GPIO.output(LEFT_BACK_PORT[0],False)
            GPIO.output(LEFT_BACK_PORT[1],True)
            print ("执行指令:右转向")
        else:
            GPIO.output(RIGHT_FRONT_PORT[0],False)
            GPIO.output(RIGHT_FRONT_PORT[1],True)
            GPIO.output(LEFT_BACK_PORT[0],True)
            GPIO.output(LEFT_BACK_PORT[1],False)
            print ("执行指令:右转倒车")
    #前进挡
    def allMove():
        GPIO.output(LEFT_FRONT_PORT[0],True)
        GPIO.output(LEFT_FRONT_PORT[1],False)
        GPIO.output(LEFT_BACK_PORT[0],True)
        GPIO.output(LEFT_BACK_PORT[1],False)
        GPIO.output(RIGHT_FRONT_PORT[0],True)
        GPIO.output(RIGHT_FRONT_PORT[1],False)
        GPIO.output(RIGHT_BACK_PORT[0],True)
        GPIO.output(RIGHT_BACK_PORT[1],False)
        print ("执行指令:前进")
    #倒车挡
    def allBack():
        GPIO.output(LEFT_FRONT_PORT[0],False)
        GPIO.output(LEFT_FRONT_PORT[1],True)
        GPIO.output(LEFT_BACK_PORT[0],False)
        GPIO.output(LEFT_BACK_PORT[1],True)
        GPIO.output(RIGHT_FRONT_PORT[0],False)
        GPIO.output(RIGHT_FRONT_PORT[1],True)
        GPIO.output(RIGHT_BACK_PORT[0],False)
        GPIO.output(RIGHT_BACK_PORT[1],True)
        print ("执行指令:后退")
    #刹车
    def stop():
        GPIO.output(LEFT_FRONT_PORT[0],False)
        GPIO.output(LEFT_FRONT_PORT[1],False)
        GPIO.output(LEFT_BACK_PORT[0],False)
        GPIO.output(LEFT_BACK_PORT[1],False)
        GPIO.output(RIGHT_FRONT_PORT[0],False)
        GPIO.output(RIGHT_FRONT_PORT[1],False)
        GPIO.output(RIGHT_BACK_PORT[0],False)
        GPIO.output(RIGHT_BACK_PORT[1],False)
        print ("执行指令:停止")

