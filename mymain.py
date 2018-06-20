#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import numpy as np
from numpy import random as nr
import xlrd
#===对excel等数据读取====
ExcelFile=xlrd.open_workbook(r'input_node.xlsx')
sheet1_name=ExcelFile.sheet_names()[0]
sheet1=ExcelFile.sheet_by_index(0)
#所有包裹重量和体积
weight=sheet1.col_values(4)
volume=sheet1.col_values(5)
#收件时间

#=====================
#定义truck类
class Truck:
    def __init__(self,load,volume,distance,tdistance,time,cost,type,current): #卡车初始化
        self.load=load
        self.volume=volume
        self.distance = distance
        self.tdistance =tdistance
        self.time = time
        self.cost = cost
        self.type=type  #随机选择一个车类型
        self.current=current
#=====================
N=1000 #商家数量
la=1 #参数lambda
cite=np.arange(1,1001,1)
#=====================
iteration=500 #迭代最大次数
M=1
if M<iteration:
    s=float("inf")
    remain=cite
    routeA=[]
    routeB=[]
    s_cost=0
    if remain.any(): #当remain不为空
        truck=Truck(0,0,0,0,0,0,nr.randint(1,3,(1,1)),0)   #生成一个truck对象
        route=[]
        if truck.current!=0: #没有返回配送点
            [route,remian]=find_node(truck,route,remain,la,iteration)
            remain=set(remian).difference(truck.current)
            route.append(truck.current)
        if truck.type==1:
            routeA.append(route)
        else:
            routeB.append(route)
        s_cost=s_cost+1
    if s_cost<s:
        s=s_cost
        la=max(la-1,1)
    else:
        la=la+1
    M=M+1
    # 大循环结束



