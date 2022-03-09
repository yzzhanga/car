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


fire()