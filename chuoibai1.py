# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:29:50 2024

@author: Student
"""

x="Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
s1=x.split(", ")
print("Bảng 1")
for a in s1:
    print(a)
print('')   
print("Bảng 2")
s2=x.replace(" P.","").replace(" Q.","").replace(" Tp.","")
s3=s2.split(", ")
for c in s3:
    print(c)
