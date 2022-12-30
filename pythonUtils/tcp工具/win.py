import tkinter as tk
import tcp
import config
from tkinter import *
from tkinter import ttk
'''窗口参数'''

class App:
  def __init__(self, window):

      def send():
          getMsg.delete(1.0, END)
          print("发送数据" + ipcom.get() + ":" + portcom.get())
          response = tcp.tcpSend(ipcom.get(),portcom.get(),encom.get(),setMsg.get())
          getMsg.insert(1.0, response)

      #IP框
      ipVariable = tk.StringVar()
      #创建下拉菜单
      ipcom = ttk.Combobox(window, textvariable=ipVariable)
      ipcom.pack()
      #给下拉菜单设定值
      ipcom["value"] = config.getIp()
      #下拉菜单的默认值
      ipcom.current(0)    
      def ipFunc(event):
        #print(ipcom.get())            # #获取选中的值方法1
        print(ipVariable.get())      # #获取选中的值方法2
        #给下拉菜单绑定事件
      ipcom.bind("<<ComboboxSelected>>", ipFunc)
        
      #端口框
      portVariable = tk.StringVar()
      portcom = ttk.Combobox(window, textvariable=portVariable)
      portcom.pack()
      portcom["value"] = config.getPort()
      portcom.current(0)    
      def xFunc(event):
        print(portVariable.get())
      portcom.bind("<<ComboboxSelected>>", xFunc)
          
      #编码框
      enVariable = tk.StringVar()
      encom = ttk.Combobox(window, textvariable=enVariable)
      encom.pack()
      encom["value"] = ["utf8", "gbk", "base64"]    
      encom.current(0)    
      def enFunc(event):
        print(enVariable.get())
      encom.bind("<<ComboboxSelected>>", enFunc)
        
      #发送框
      setMsg = Entry(window,justify=LEFT,width=1000)
      setMsg.pack(padx=10, pady=10)
      setMsg.delete(0, END)
      setMsg.insert(0, "")
      
      frame = tk.Frame(window)
      frame.pack()
      '''self.openBU = tk.Button(frame, text="建立连接", fg="blue", command=open,width=6,height=1)
      self.openBU.pack(side=tk.LEFT)
      self.closeBU = tk.Button(frame, text="关闭连接", fg="blue", command=close,width=6,height=1)
      self.closeBU.pack(side=tk.LEFT)'''
      self.sendBU = tk.Button(frame, text="发送", fg="blue", command=send,width=6,height=1)
      self.sendBU.pack(side=tk.LEFT)
      
      #接收框
      getMsg = Text(window, width=1000,height=1000)
      getMsg.pack(padx=10, pady=10)
      #1行0列-末尾
      getMsg.delete(1.0, END)

