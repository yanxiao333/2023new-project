#!/usr/bin/env python39
# -*- coding:utf-8 -*-
#二收房数据分析事例
import tkinter as tk

if __name__ == "__main__":
    window=tk.Tk() #创新一个窗体的对象
    window.title('二手房数据分析')
    #设置窗体的宽高
    window.geometry('690*390')
    canvas = tk.Canvas(window,width=690,height=390)
    #创建一个图片对象
    img_file=tk.PhotoImage(file="img/背景.png")
    canvas.pack()

    #显示窗体
    window.mainloop()
