import tkinter as tk
import os
window = tk.Tk()
window.title("航航献爱心")
window.geometry("400x200")
txt = tk.StringVar()
txt0 = tk.StringVar()
txt.set("点击按钮")
times = -1

def touch():
    global times
    if times == -1:
        os.system("shutdown -s -t 300")     
    txt.set("对不起，点击100次按钮取消关机")
    times += 1
    txt0.set("当前点击次数："+str(times))    
    if times >= 100:
        os.system("shutdown -a")
        txt.set("关闭成功，请退出")

message = tk.Label(window, textvariable=txt,width=40,height=5,font=12)
b = tk.Button(window,text="点我有惊喜",command=touch)
time = tk.Label(window,textvariable=txt0,width=100,height=5,font=12)
message.pack()
b.pack()
time.pack()

window.mainloop()