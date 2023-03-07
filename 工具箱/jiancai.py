import os
from tkinter import *
from tkinter.messagebox import showerror

from PIL import ImageTk,Image


def jiancai():
    im1=None
    photo=None
    im2=None
    def xianshi():
        def qiege():
            try:
                images_list = [im2.crop((c[-1], a[-1], d[-1], b[-1]))]

                def save_images(image_list):

                    """ 保存 正中央的照片图片 """
                    output_path = os.path.abspath(os.path.dirname(__file__))
                    for index, image in enumerate(image_list):
                        image.save(f"{output_path}/{index + 1}.jpg", "jpg")

                    def tuichu():
                        roots.destroy()

                    root.destroy()
                    roots = Tk()
                    # 禁止窗口拉伸
                    roots.resizable(width=False, height=False)
                    roots.geometry('300x300')
                    label = Label(roots, text='''裁剪成功!
        快去查看图片吧~ ^_^
        注:图片在工具箱的目录里''', font=('迷你简毡笔黑', 15), fg='red')

                    button = Button(roots, activeforeground='aqua', relief=FLAT, activebackground='steelblue',
                                    bg="steelblue", fg="aqua", text='确定', font=('迷你简毡笔黑', 10), command=tuichu)
                    label.pack(pady=20)
                    button.pack(pady=10)
                    root.mainloop()

                save_images(images_list)
            except SystemError:
                mx3 = showerror(title='错误消息框', message='请正确裁剪')
                root.destroy()
        contents=entry.get()
        try:
            im1=Image.open(contents)
            roota.destroy()
            root=Tk()
            root.resizable(width=False, height=False)
            im2 = im1.copy()
            # 将复制后的图像进行缩放，传入一个元组
            im2.thumbnail((300, 350))
            photo = ImageTk.PhotoImage(im2)
            width,height=im2.size
            root.geometry(str(100 + width) + 'x' + str(150 + height))
            frame = Frame(root, bd=1, relief=SUNKEN)
            label = Label(root, fg='red', text='''中心区域才是
            裁剪的内容哦~ ^-^
            线之间不能重合哟~''', font=('迷你简毡笔黑', 15))
            button3 = Button(root, activeforeground='aqua', relief=FLAT, activebackground='steelblue', bg="steelblue",
                         fg="aqua", text='开始切割', font=('迷你简毡笔黑', 10), command=qiege)
            w = Canvas(frame, width=width, height=height)
            frame.pack()
            w.pack()
            button3.pack(pady=10)
            label.pack()
            a = [height / 3]
            b = [(2 * height) / 3]
            c = [width / 3]
            d = [(width * 2) / 3]

            def paint(event):
                x, y = event.x, event.y
                if a[-1] - 5 <= y <= a[-1] + 5 and 1 < y < height - 1: #说明在第一条线附件
                    a.append(y)
                    w.coords(line1, 0, a[-1], width, a[-1])
                    w.itemconfig(line1, fill="aqua", dash=(255, 255))
                if b[-1] - 10 <= y <= b[-1] + 10 and 1 < y < height - 1:
                    b.append(y)
                    w.coords(line2, 0, b[-1], width, b[-1])
                    w.itemconfig(line2, fill="aqua", dash=(255, 255))
                if c[-1] - 5 <= x <= c[-1] + 5 and 1 < x < width + 1:
                    c.append(x)
                    w.coords(line3, c[-1], 0, c[-1], height)
                    w.itemconfig(line3, fill="aqua", dash=(255, 255))
                if d[-1] - 10 <= x <= d[-1] + 10 and 1 < x < width + 1:
                    d.append(x)
                    w.coords(line4, d[-1], 0, d[-1], height)
                    w.itemconfig(line4, fill="aqua", dash=(255, 255))
            w.bind("<B1-Motion>", paint)
            w.create_image(width / 2, height / 2, image=photo)
            line1 = w.create_line(0, (height) / 3, width, (height) / 3, fill="red", dash=(4, 4))
            line2 = w.create_line(0, (2 * height) / 3, width, (2 * height) / 3, fill="red", dash=(4, 4))
            line3 = w.create_line(width / 3, 0, width / 3, height, fill="red", dash=(4, 4))
            line4 = w.create_line((width * 2) / 3, 0, (2 * width) / 3, height, fill="red", dash=(4, 4))
            mainloop()
        except (FileNotFoundError, OSError):
            mx3 = showerror(title='错误消息框', message='找不到图片，请仔细检查地址是否有误！')

    roota=Tk()
    roota.resizable(width=False,height=False)
    frame=Frame(roota,bd=1,relief=SUNKEN,background='plum')
    button=Button(frame,activebackground='aqua',relief=FLAT,activeforeground='steelblue',bg='steelblue',
                  fg='aqua',text='确定',font=('迷你简毡笔黑',10),command=xianshi)
    label=Label(frame,text='''请输入图片地址:
     粘贴请 ctrl+v 
    ''',font=('迷你简毡笔黑', 10), fg="mediumvioletred")
    entry = Entry(frame, width=30, fg="mediumvioletred", background='plum', font=('迷你简毡笔黑', 10))
    label.pack(side=TOP)
    entry.pack(padx=10,pady=30)
    frame.pack()
    button.pack(side=BOTTOM)
    mainloop()


