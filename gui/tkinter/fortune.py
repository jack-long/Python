#!/usr/bin/env python
# -*- coding: utf-8 -*-

## 文字大小、颜色
## 分割线

from Tkinter import *
import ttk
import time
from random import randint

root = Tk()
root.title("双色球")

frame = ttk.Frame(root, padding=(10,10))
frame.grid(column=0, row=0, sticky=(N,S,E,W))

title = ttk.Label(frame, text="双色球")
# time
timevar = DoubleVar()
timevar.set(time.strftime("%Y-%m-%d", time.gmtime()))

r1 = StringVar()
r2 = StringVar()
r3 = StringVar()
r4 = StringVar()
r5 = StringVar()
r6 = StringVar()
blue = StringVar()

numbers = [r1, r2, r3, r4, r5, r6, blue]
for each in numbers:
    each.set('')

def go(numbers):
    numlist = []
    for num in range(1,7):
        randnum = randint(1,33)
        # 'in' check
        while randnum in numlist:
            randnum = randint(1,33)
        numlist.append(randnum)
        numlist.sort()
    for num in range(6):
        numbers[num].set(str(numlist[num]).zfill(2))
    numbers[-1].set(str(randint(1,16)).zfill(2))
pick = ttk.Button(frame, text="选号", command=lambda numbers=numbers: go(numbers))    
time = ttk.Label(frame, border=2, relief="sunken", textvariable=timevar)
n0 = ttk.Entry(frame, width=2, textvariable=r1)
n1 = ttk.Entry(frame, width=2, textvariable=r2)
n2 = ttk.Entry(frame, width=2, textvariable=r3)
n3 = ttk.Entry(frame, width=2, textvariable=r4)
n4 = ttk.Entry(frame, width=2, textvariable=r5)
n5 = ttk.Entry(frame, width=2, textvariable=r6)
n6 = ttk.Entry(frame, width=2, textvariable=blue)
ok = ttk.Button(frame, text="确定")
s = ttk.Separator(frame, orient=VERTICAL)

title.grid(column=3, row=0, columnspan=5, sticky=(W,N), pady=10)
time.grid(column=0, row=1, columnspan=4, sticky=(W,N), pady=5)
pick.grid(column=5, row=1, columnspan=2, rowspan=2, sticky=(N,E), pady=5)
n0.grid(column=0, row=3, padx=5, pady=5)
n1.grid(column=1, row=3, padx=5, pady=5)
n2.grid(column=2, row=3, padx=5, pady=5)
n3.grid(column=3, row=3, padx=5, pady=5)
n4.grid(column=4, row=3, padx=5, pady=5)
n5.grid(column=5, row=3, padx=5, pady=5)
s.grid(column=6, row=3)
n6.grid(column=7, row=3, padx=5, pady=5)
#ok.grid(column=5, row=4, columnspan=2, rowspan=2, sticky=(N,E))

root.mainloop()
