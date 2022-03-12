#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep
import orderSet 

order = orderSet.order()

def fire():
    print("执行指令")
    order.forword()
    sleep(2)
    order.stop()
    
    order.backword()
    sleep(2)
    order.stop()
    
    order.turnright()
    sleep(2)
    order.stop()

    order.turnleft()
    sleep(2)
    order.stop()
    
    order.backleft()
    sleep(2)
    order.stop()

    order.backright()
    sleep(2)
    order.stop()

fire()
