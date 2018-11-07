# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:02:47 2018

@author: yağmur
"""

#matris icin

matris=int(input("birsayigirin"))


for i in range(matris):
    print(("0"*i) + ("1"*1) + "0"*(matris-i-1))