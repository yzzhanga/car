#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO



class L298nOrder:
    # LEFT_FRONT_PORT  #左前轮 正负输出，这两个输出互斥，不能同时为正，但可以同时为负，不管同时为正或负，都视为刹车；
    # LEFT_BACK_PORT #左后轮
    # RIGHT_FRONT_PORT #右前轮
    # RIGHT_BACK_PORT  #右后轮

    def __init__(self,lp = [10,17],lb= [27,22],rp= [18,23],rb= [24,25]):
        self.LEFT_FRONT_PORT = lp
        self.LEFT_BACK_PORT = lb
        self.RIGHT_FRONT_PORT = rp
        self.RIGHT_BACK_PORT = rb

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.setup()
        print("指令集初始化成功")

    def setup(self):
        GPIO.setup(self.LEFT_FRONT_PORT,GPIO.OUT)
        GPIO.setup(self.LEFT_BACK_PORT,GPIO.OUT)
        GPIO.setup(self.RIGHT_FRONT_PORT,GPIO.OUT)
        GPIO.setup(self.RIGHT_BACK_PORT,GPIO.OUT)

    #关闭GPIO的输出设置（这里有个前提是GPIO全部服务本集合，右可能会误关闭其他GPIO组合程序）
    def destory(self):
        print("指令驱动销毁")
        GPIO.cleanup()

    #转向程序 左中心线的顺时针和逆时针旋转
    def turnLeftRound(self,leftBool):
        if (leftBool):
            GPIO.output(self.LEFT_FRONT_PORT[0],    True)
            GPIO.output(self.LEFT_FRONT_PORT[1],    False)
            GPIO.output(self.RIGHT_BACK_PORT[0],    False)
            GPIO.output(self.RIGHT_BACK_PORT[1],    True)
            print ("执行指令:左转向")
        else:
            GPIO.output(self.LEFT_FRONT_PORT[0],    False)
            GPIO.output(self.LEFT_FRONT_PORT[1],    True)
            GPIO.output(self.RIGHT_BACK_PORT[0],    True)
            GPIO.output(self.RIGHT_BACK_PORT[1],    False)
            print ("执行指令:左转倒车")
    #转向程序 右中心线的顺时针和逆时针旋转
    def turnRightRound(self,rightBool):
        if (rightBool):
            GPIO.output(self.RIGHT_FRONT_PORT[0],   True)
            GPIO.output(self.RIGHT_FRONT_PORT[1],   False)
            GPIO.output(self.LEFT_BACK_PORT[0],     False)
            GPIO.output(self.LEFT_BACK_PORT[1],     True)
            print ("执行指令:右转向")
        else:
            GPIO.output(self.RIGHT_FRONT_PORT[0],   False)
            GPIO.output(self.RIGHT_FRONT_PORT[1],   True)
            GPIO.output(self.LEFT_BACK_PORT[0],     True)
            GPIO.output(self.LEFT_BACK_PORT[1],     False)
            print ("执行指令:右转倒车")
    #前进挡
    def allMove(self):
        GPIO.output(self.LEFT_FRONT_PORT[0],        True)
        GPIO.output(self.LEFT_FRONT_PORT[1],        False)
        GPIO.output(self.LEFT_BACK_PORT[0],         True)
        GPIO.output(self.LEFT_BACK_PORT[1],         False)
        GPIO.output(self.RIGHT_FRONT_PORT[0],       True)
        GPIO.output(self.RIGHT_FRONT_PORT[1],       False)
        GPIO.output(self.RIGHT_BACK_PORT[0],        True)
        GPIO.output(self.RIGHT_BACK_PORT[1],        False)
        print ("执行指令:前进")
    #倒车挡
    def allBack(self):
        GPIO.output(self.LEFT_FRONT_PORT[0],        False)
        GPIO.output(self.LEFT_FRONT_PORT[1],        True)
        GPIO.output(self.LEFT_BACK_PORT[0],         False)
        GPIO.output(self.LEFT_BACK_PORT[1],         True)
        GPIO.output(self.RIGHT_FRONT_PORT[0],       False)
        GPIO.output(self.RIGHT_FRONT_PORT[1],       True)
        GPIO.output(self.RIGHT_BACK_PORT[0],        False)
        GPIO.output(self.RIGHT_BACK_PORT[1],        True)
        print ("执行指令:后退")
    #刹车
    def stop(self):
        GPIO.output(self.LEFT_FRONT_PORT[0],        False)
        GPIO.output(self.LEFT_FRONT_PORT[1],        False)
        GPIO.output(self.LEFT_BACK_PORT[0],         False)
        GPIO.output(self.LEFT_BACK_PORT[1],         False)
        GPIO.output(self.RIGHT_FRONT_PORT[0],       False)
        GPIO.output(self.RIGHT_FRONT_PORT[1],       False)
        GPIO.output(self.RIGHT_BACK_PORT[0],        False)
        GPIO.output(self.RIGHT_BACK_PORT[1],        False)
        print ("执行指令:停止")

    def opt(self,_inputOrder):
        retval = 1;
        # _inputOrder = input('请输入底盘指令:w-前进,s-后退,a-向左,d-向右,z-左倒车,c-右倒车,x-刹车,p-销毁终止指令:')
        if (_inputOrder == "w"):
            self.stop()
            self.allMove()
        if (_inputOrder == "s"):
            self.stop()
            self.allBack()
        if (_inputOrder == "a"):
            self.stop()
            self.turnLeftRound(False)
        if (_inputOrder == "d"):
            self.stop()
            self.turnRightRound(False)
        if (_inputOrder == "z"):
            self.stop()
            self.turnLeftRound(True)
        if (_inputOrder == "c"):
            self.stop()
            self.turnRightRound(True)
        if (_inputOrder == "x"):
            self.stop()
        if (_inputOrder == "p"):
            self.destory()
            retval =0
        return retval
