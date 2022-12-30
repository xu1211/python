import tkinter as tk
import win
from tkinter import *
from tkinter import ttk


# 根窗口
window = tk.Tk()
window.title("tcp工具")
window.geometry("600x400")
window.geometry("+500+200")


app = win.App(window)

# 开始主事件循环
window.mainloop()