import tkinter as tk
import tkinter.messagebox
def main(title,size="400x200",choice=True):
    '''最小GUI开发框架'''
    #为基础设置
    window = tk.Tk()
    window.title(title)
    window.geometry(size)
    window.resizable(width=choice,height=choice)

    #函数定义
    def info():
        info = tk.messagebox.showinfo('关于','作者：航航\nQQ:550653451')

    #菜单选项
    member = tk.Menu(window)
    filemenu = tk.Menu(member,tearoff=0)
    member.add_cascade(label="选项",menu=filemenu)
    filemenu.add_command(label="关于",command=info)

    #基本控件
    a = tk.Label(window,text="---你可以在关于中找到作者的信息---",font=1) #修改源码请删除
    a.pack(side="bottom")
    message = tk.Label(window, textvariable=txt,width=40,height=5,font=12)
    b = tk.Button(window,text="点我有惊喜",command=touch)
    time = tk.Label(window,textvariable=txt0,width=100,height=5,font=12)
    message.pack()
    b.pack()
    time.pack()


    window.config(menu=member)
    window.mainloop()

main('测试')
    




