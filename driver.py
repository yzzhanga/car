#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep
import orderSet

#加载指令集
order = orderSet.L298nOrder
#装载GPIO输出初始化
order.setup()
#底盘自检程序
def test():
    print("执行指令")
    order.allMove()
    sleep(2)
    order.stop()

    order.allBack()
    sleep(2)
    order.stop()

    order.turnLeftRound(True)
    sleep(2)
    order.stop()

    order.turnLeftRound(False)
    sleep(2)
    order.stop()


    order.turnRightRound(True)
    sleep(2)
    order.stop()

    order.turnRightRound(False)
    sleep(2)
    order.stop()
#自检程序执行
test()


_inputOrder = 'x'
while True :
    sleep(0.5)
    _inputOrder = input('请输入底盘指令:w-前进,s-后退,a-向左,d-向右,z-左倒车,c-右倒车,x-刹车,p-销毁终止指令,o-重新安装指令:')
    if (_inputOrder == 'w'):
        order.stop()
        order.allMove()
    if (_inputOrder == 's'):
        order.stop()
        order.allBack()
    if (_inputOrder == 'a'):
        order.stop()
        order.turnLeftRound(False)
    if (_inputOrder == 'd'):
        order.stop()
        order.turnRightRound(False)
    if (_inputOrder == 'z'):
        order.stop()
        order.turnLeftRound(True)
    if (_inputOrder == 'c'):
        order.stop()
        order.turnRightRound(True)
    if (_inputOrder == 'x'):
        order.stop()
    if (_inputOrder == 'p'):
        order.destory()
    if (_inputOrder == 'o'):
        order.setup()
