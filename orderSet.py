#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep
import RPi.GPIO as GPIO

point = [5,6,16,26]

class L298nOrder:
    
    def __init__(self) -> print("指令集初始化成功"):
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup   
        GPIO.setup(point,GPIO.OUT)
        pass

    def leftMove(self,bool):
        GPIO.output(point[0],bool)
    def leftBack(self,bool):
        GPIO.output(point[1],bool)

    def rightMove(self,bool):
        GPIO.output(point[2],bool)

    def rightBack(self,bool):
        GPIO.output(point[3],bool)

    def allMove(self,_isMove):
       GPIO.output(point[0],_isMove)
       GPIO.output(point[2],_isMove)
    
    def allBack(self,_isMove):
        GPIO.output(point[1],_isMove)
        GPIO.output(point[3],_isMove)
  
_order = L298nOrder()

class order:
   
    #指令方法
    def stop(self):
        _order.allMove(False)
        _order.allBack(False)
        print ("执行指令:停止")


    def forword(self):
        _order.allMove(True)
        print ("执行指令:前进")

    def backword(self):
        _order.allBack(True)
        print ("执行指令:后退")
    
    def turnleft(self):
        _order.rightMove(True)
        print ("执行指令:左转")

    def turnright(self):
        _order.leftMove(True)
        print ("执行指令:右转")

    def backleft(self):
        _order.rightBack(True)
        print ("执行指令:左退")

    def backright(self):
        _order.leftBack(True)
        print ("执行指令:右退")


        
      


