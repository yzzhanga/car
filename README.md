# 自家做的智能小车底盘驱动程序
  由于小车底盘使用了两组L298N控制器控制了四个轮子马达，所以指令集里会出现四组接口参数；

## Driver.py
 是小车的驱动入口，使用python3.8 （非树莓派环境请使用模拟器RPi.GPIO-def来模拟树莓派环境）
 Driver程序里分为两组函数，第一组是自检程序，主要是校验小车加载指令集后是否正确
 第二组是指令输入函数，主要是在没有其他输入部件的情况下教会同学们如何使用指令集
## OrderSet.py
  封装了底盘的L298N控制器接线驱动