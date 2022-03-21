#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep
import redis

# 连接接收指令队列的工具，之所以使用服务器队列主要是我写服务端程序比较顺手，无他……(`へ´*)ノ
class mqutils:

    def __init__(self,host,port,password,db):
        self.host = host
        self.port = port
        self.password = password
        self.db = db

    def connection(self):
        redis_pool = redis.ConnectionPool(host=self.host, port= self.port, password= self.password, db= self.db)
        self.instance = redis.Redis(connection_pool= redis_pool)

    def receive(self,name,orderOpt):
        redisSev = self.instance;
        while True:
            if redisSev.llen(name) == 0 :
                sleep(0.5)
                continue
            # 收到指令后反序列化字符串，之所以是反序列化，因为服务端使用的StringRedisSerializer器，我懒得改别的类型了。╭(╯^╰)╮
            order =  str(redisSev.rpop(name), encoding = "utf-8")
            print(" <')))><<} ---[收到指令]:",order)
            status  = orderOpt.opt(order)
            if status == 0 :
                break