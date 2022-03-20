#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep
from orderSet import L298nOrder

#加载指令集
order = L298nOrder([10,17],[27,22],[18,23], [24,25])
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
while True:
    sleep(0.5)
    _inputOrder = input('请输入底盘指令:w-前进,s-后退,a-向左,d-向右,z-左倒车,c-右倒车,x-刹车,p-销毁终止指令:')
    if (_inputOrder == 'w'):
        order.stop()
        order.allMove()
        continue
    if (_inputOrder == 's'):
        order.stop()
        order.allBack()
        continue
    if (_inputOrder == 'a'):
        order.stop()
        order.turnLeftRound(False)
        continue
    if (_inputOrder == 'd'):
        order.stop()
        order.turnRightRound(False)
        continue
    if (_inputOrder == 'z'):
        order.stop()
        order.turnLeftRound(True)
        continue
    if (_inputOrder == 'c'):
        order.stop()
        order.turnRightRound(True)
        continue
    if (_inputOrder == 'x'):
        order.stop()
        continue
    if (_inputOrder == 'p'):
        order.destory()
        break
