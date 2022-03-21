#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep
from orderSet import L298nOrder
from communication import mqutils

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



redis = mqutils(host='**********', port= 46379, password= '********', db= 0)
redis.connection()

redis.receive("car_order_queue",order)