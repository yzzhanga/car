#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import logging
#针对麦克纳姆轮进行了指令改良，增加了侧平移，原地转向和斜向移动，增加了小车的灵活性
logging.getLogger().setLevel(logging.INFO)

class L298nOrder:
    # LEFT_FRONT_PORT  #左前轮 正负输出，这两个输出互斥，不能同时为正，但可以同时为负，不管同时为正或负，都视为刹车；
    # LEFT_BACK_PORT #左后轮
    # RIGHT_FRONT_PORT #右前轮
    # RIGHT_BACK_PORT  #右后轮

    def __init__(self,  lp,   lb, rp, rb):
        self.LEFT_FRONT_PORT = lp
        self.LEFT_BACK_PORT = lb
        self.RIGHT_FRONT_PORT = rp
        self.RIGHT_BACK_PORT = rb

        self.setup()
        self.setting()
        logging.info("指令集初始化成功")

    #设置针脚的初始状态
    def setup(self):
        # GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.LEFT_FRONT_PORT,GPIO.OUT)
        GPIO.setup(self.LEFT_BACK_PORT,GPIO.OUT)
        GPIO.setup(self.RIGHT_FRONT_PORT,GPIO.OUT)
        GPIO.setup(self.RIGHT_BACK_PORT,GPIO.OUT)
        logging.info("端口初始完成")


    #置位
    def setting(self):
        GPIO.output(self.LEFT_FRONT_PORT[0],    False)
        GPIO.output(self.LEFT_FRONT_PORT[1],    False)
        GPIO.output(self.LEFT_BACK_PORT[0],     False)
        GPIO.output(self.LEFT_BACK_PORT[1],     False)
        GPIO.output(self.RIGHT_FRONT_PORT[0],   False)
        GPIO.output(self.RIGHT_FRONT_PORT[1],   False)
        GPIO.output(self.RIGHT_BACK_PORT[0],    False)
        GPIO.output(self.RIGHT_BACK_PORT[1],    False)
        logging.info("置位完成")

    def ahead(self):
        self.setting()                                    #状态置位，确保指令正确
        GPIO.output(self.LEFT_FRONT_PORT[0],    True)   #左前轮正向高电平
        GPIO.output(self.LEFT_BACK_PORT[0],     True)   #左后轮正向高电平
        GPIO.output(self.RIGHT_FRONT_PORT[0],   True)   #右前轮正向高电平
        GPIO.output(self.RIGHT_BACK_PORT[0],    True)   #右后轮正向高电平
        logging.info("执行指令:前进")

    def behand(self):
        self.setting()
        GPIO.output(self.LEFT_FRONT_PORT[1],    True)   #左前轮反向高电平
        GPIO.output(self.LEFT_BACK_PORT[1],     True)   #左后轮反向高电平
        GPIO.output(self.RIGHT_FRONT_PORT[1],   True)   #右前轮反向高电平
        GPIO.output(self.RIGHT_BACK_PORT[1],    True)   #右后轮反向高电平
        logging.info("执行指令:倒车")

    def left_sideway(self):
        self.setting()  # 状态置位，确保指令正确
        GPIO.output(self.LEFT_FRONT_PORT[1],    True)  # 左前轮反向高电平
        GPIO.output(self.LEFT_BACK_PORT[0],     True)  # 左后轮正向高电平
        GPIO.output(self.RIGHT_FRONT_PORT[0],   True)  # 右前轮正向高电平
        GPIO.output(self.RIGHT_BACK_PORT[1],    True)  # 右后轮反向高电平
        logging.info("执行指令:左平移")

    def right_sideway(self):
        self.setting()  # 状态置位，确保指令正确
        GPIO.output(self.LEFT_FRONT_PORT[0],    True)  # 左前轮正向高电平
        GPIO.output(self.LEFT_BACK_PORT[1],     True)  # 左后轮反向高电平
        GPIO.output(self.RIGHT_FRONT_PORT[1],   True)  # 右前轮反向高电平
        GPIO.output(self.RIGHT_BACK_PORT[0],    True)  # 右后轮正向高电平
        logging.info("执行指令:右平移")

    def left_diagonal(self,direction=0):
        self.setting()  # 状态置位，确保指令正确
        GPIO.output(self.LEFT_BACK_PORT[direction],     True)  # 左后轮正向高电平；方向为1则取反向
        GPIO.output(self.RIGHT_FRONT_PORT[direction],   True)  # 右前轮正向高电平；方向为1则取反向
        logging.info("执行指令:左斜角")

    def right_diagonal(self,direction=0):
        self.setting()  # 状态置位，确保指令正确
        GPIO.output(self.LEFT_FRONT_PORT[direction],    True)  # 左前轮正向高电平；方向为1则取反向
        GPIO.output(self.RIGHT_BACK_PORT[direction],    True)  # 右后轮正向高电平；方向为1则取反向
        logging.info("执行指令:右斜角")

    def left_concerning(self):
        self.setting()  # 状态置位，确保指令正确
        GPIO.output(self.RIGHT_FRONT_PORT[0],   True)  # 右前轮正向高电平
        GPIO.output(self.RIGHT_BACK_PORT[0],    True)  # 右后轮正向高电平
        logging.info("执行指令:左转")

    def right_concerning(self):
        self.setting()  # 状态置位，确保指令正确
        GPIO.output(self.LEFT_FRONT_PORT[0],    True)  # 左前轮正向高电平
        GPIO.output(self.LEFT_BACK_PORT[0],     True)  # 左后轮正向高电平
        logging.info("执行指令:右转")

    def right_turnround(self):
        self.setting()  # 状态置位，确保指令正确
        GPIO.output(self.LEFT_FRONT_PORT[0],    True)  # 左前轮正向高电平
        GPIO.output(self.LEFT_BACK_PORT[0],     True)  # 左后轮正向高电平
        GPIO.output(self.RIGHT_FRONT_PORT[1],   True)  # 右前轮正向高电平
        GPIO.output(self.RIGHT_BACK_PORT[1],    True)  # 右后轮正向高电平
        logging.info("执行指令:掉头（右侧方向）")

    def turn_of_rear_axis(self):
        self.setting()  # 状态置位，确保指令正确
        GPIO.output(self.LEFT_FRONT_PORT[0],    True)  # 左前轮正向高电平
        GPIO.output(self.RIGHT_FRONT_PORT[1],   True)  # 右前轮正向高电平
        logging.info("执行指令:后轴转动（右侧方向）")

    def opt(self,_inputOrder):
        retval = 1;
        # _inputOrder = input('请输入底盘指令:w-前进,s-后退,a-向左,d-向右,z-左倒车,c-右倒车,x-刹车,p-销毁终止指令:')
        if (_inputOrder == "w"):
            self.ahead()
        if (_inputOrder == "s"):
            self.behand()
        if (_inputOrder == "a"):
            self.left_sideway()
        if (_inputOrder == "d"):
            self.right_sideway()
        if (_inputOrder == "q"):
            self.left_diagonal(0)
        if (_inputOrder == "e"):
            self.right_diagonal(0)
        if (_inputOrder == "z"):
            self.left_diagonal(1)
        if (_inputOrder == "c"):
            self.right_diagonal(1)
        if (_inputOrder == "x"):
            self.setting()
        if (_inputOrder == "r"):
            self.left_concerning()
        if (_inputOrder == "t"):
            self.right_concerning()
        if (_inputOrder == "g"):
            self.right_turnround()
        if (_inputOrder == "f"):
            self.turn_of_rear_axis()
        return retval

def test():
     order = L298nOrder((14,11,),(25,26),(13,15),(24,26))
     order.left_concerning()
test()