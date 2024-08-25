# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:22:37 2024

@author: nguyenthuythaovy
"""

a=int(input("Nhập giờ:"))
if 1<=a<=12:
    b=int(input("Nhập phút:"))
    if 1<=b<=60:
        c=int(input("Nhập giây:"))
        if 1<=c<=60:
            x=a*3600
            y=b*60
            print("Số giây của thời gian trên:",c+x+y)
        else:
            print("Số giây không quá 60")
    else:
        print("Số phút không quá 60")
else:
    print("Số giờ không quá 12")
    
