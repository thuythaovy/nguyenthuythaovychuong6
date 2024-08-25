# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:24:17 2024

@author: Thụy Thảo Vy
"""

import math
a=float(input("Nhập số thực a:"))
b=float(input("Nhập số thực b:"))
x=(math.sqrt(a)-math.sqrt(b))/(math.pow(a,1/4)-math.pow(b,1/4))-(math.sqrt(a)+math.pow(a*b,1/4))/(math.pow(a,1/4)+math.pow(b,1/4))
print("Kết quả:",x)
