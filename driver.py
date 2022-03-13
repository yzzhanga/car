#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep
import orderSet

order = orderSet.L298nOrder
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

test()


_inputOrder = 'x'
while True :
    sleep(0.5)
    _inputOrder = input('请输入底盘指令:w-前进,s-后退,a-向左,d-向右,z-左倒车,c-右倒车,x-刹车:')
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