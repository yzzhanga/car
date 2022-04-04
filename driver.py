#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from orderSet import L298nOrder
from communication import mqutils

#加载指令集
order =L298nOrder([26,19],[13,10],[21,20], [16,12])
redis =mqutils(host='mq.yzzhanga.xyz', port= 46379, password= '1qaz2wsx', db= 0)
redis.connection()

redis.receive("car_order_queue",order)