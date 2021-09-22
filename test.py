# -*- coding: utf-8 -*- 
import os 
import sys
import pyupbit

access = "JtdrqgUURH5IdpiLhva7WSqARaZhEpsaMAxhIe3k"          # 본인 값으로 변경
secret = "u4d4LmDDhB2illrH3Stdfqfv3m7CMxdMKd8UiEwl"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회