import time
import RPi.GPIO as gpio
import logging
logging.getLogger().setLevel(logging.INFO)

PSB_SELECT = 1
PSB_L3 = 2
PSB_R3 = 3
PSB_START = 4
PSB_PAD_UP = 5
PSB_PAD_RIGHT = 6
PSB_PAD_DOWN = 7
PSB_PAD_LEFT = 8
PSB_L2 = 9
PSB_R2 = 10
PSB_L1 = 11
PSB_R1 = 12
PSB_GREEN = 13
PSB_RED = 14
PSB_BLUE = 15
PSB_PINK = 16
PSB_TRIANGLE = 13
PSB_CIRCLE = 14
PSB_CROSS = 15
PSB_SQUARE = 26

# 右摇杆X轴数据
PSS_RX = 5
PSS_RY = 6
PSS_LX = 7
PSS_LY = 8
comd = [0x01, 0x42]  # 开始指令
data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]  # 数据存储数组

mask = [
    PSB_SELECT,
    PSB_L3,
    PSB_R3,
    PSB_START,
    PSB_PAD_UP,
    PSB_PAD_RIGHT,
    PSB_PAD_DOWN,
    PSB_PAD_LEFT,
    PSB_L2,
    PSB_R2,
    PSB_L1,
    PSB_R1,
    PSB_GREEN,
    PSB_RED,
    PSB_BLUE,
    PSB_PINK
]  # 按键值与按键说明


class PS2KEY:
    def __init__(self, DAT, CMD, CS, CLK):
        gpio.setmode(gpio.BCM)  # 选择 gpio numbers 编号系统
        gpio.setwarnings(False)
        # 设置gpio口为输出
        gpio.setup(DAT, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.setup(CMD, gpio.OUT)
        gpio.setup(CS, gpio.OUT)
        gpio.setup(CLK, gpio.OUT)
        self.DAT = DAT
        self.CMD = CMD
        self.CS = CS
        self.CLK = CLK
        self.ps2_init()
        # self.ps2_red()

    # 手柄初始化
    def ps2_init(self):
        gpio.output(self.CS, True)
        gpio.output(self.CLK, True)
        gpio.output(self.CMD, True)
        time.sleep(0.01)

    # 发送数据
    def ps2_cmd(self, cmd):
        global data
        data[1] = 0
        for ref in (1, 2, 4, 8, 16, 32, 64, 128):
            if (ref & cmd):
                gpio.output(self.CMD, True)
            else:
                gpio.output(self.CMD, False)
            gpio.output(self.CLK, True)
            time.sleep(0.00005)
            gpio.output(self.CLK, False)
            time.sleep(0.00005)
            gpio.output(self.CLK, True)
            if (gpio.input(self.DAT)):
                data[1] = ref | data[1]
        time.sleep(0.000016)

    # 判断是否为红灯模式 是--返回0 否--返回1
    def ps2_red(self):
        global data
        global comd
        gpio.output(self.CS, False)
        self.ps2_cmd(comd[0])
        self.ps2_cmd(comd[1])
        gpio.output(self.CS, True)
        if (data[1] == 57):
            return 0  # red light
        else:
            return 1  # not red

    # 读取手柄数据
    def ps2_read(self):
        global data
        global comd
        byte = 0
        ref = 0x01
        gpio.output(self.CS, False)
        self.ps2_cmd(comd[0])
        self.ps2_cmd(comd[1])
        for byte in (2, 3, 4, 5, 6, 7, 8):
            for ref in (1, 2, 4, 8, 16, 32, 64, 128):
                gpio.output(self.CLK, True)
                gpio.output(self.CLK, False)
                time.sleep(0.00005)
                gpio.output(self.CLK, True)
                if (gpio.input(self.DAT)):
                    data[byte] = ref | data[byte]
            time.sleep(0.00005)
        gpio.output(self.CS, True)

    # 清空data
    def ps2_clear(self):  # ok
        global data
        for i in range(9):
            data[i] = 0

    # 输出摇杆数据（0-255）
    def ps2_andata(self, button):
        global data
        return data[button]

    # 输出按下的按键对应编号
    def ps2_key(self):
        global data
        global mask
        self.ps2_clear()
        self.ps2_read()
        handkey = (data[4] << 8) | data[3]
        for index in range(16):
            if ((handkey & (1 << (mask[index] - 1))) == 0):
                return index + 1
        return 0



ps = PS2KEY(12,16,20,21)
while True:
    logging.info(ps.ps2_red())
    logging.info(ps.ps2_read())
    key = ps.ps2_key()
    logging.info("按键读数：%d", key)
    time.sleep(1)