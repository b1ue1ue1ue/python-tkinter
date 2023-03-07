import pygame
import sys
import requests
import json
from tkinter import*
from pygame.locals import*
import tkinter.font as tf



def fanyi():
    def cut(editor,event=None):
        editor.event_generate("<<Cut>>")
    def copy(editor, event=None):
        editor.event_generate("<<Copy>>")
    def paste(editor, event=None):
        editor.event_generate("<<Paste>>")
    def rightKey(event, editor):
        menubar.delete(0, END)
        menubar.add_command(label='剪切', command=lambda: cut(editor))
        menubar.add_command(label='复制', command=lambda: copy(editor))
        menubar.add_command(label='粘贴', command=lambda: paste(editor))
        menubar.post(event.x_root, event.y_root)
    def C():
        ent.delete(1.0,'end')
        ent2.delete(1.0,'end')
    def youdao():
        ent2.delete(1.0,'end')
        content=ent.get(1.0,'end')
        a=[]
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
        data = {}
        data['i'] = content
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = '16079142839884'
        data['sign'] = '7fa30595c70a9a765816fda28b64b9ac'
        data['lts'] = '1607914283988'
        data['bv'] = '4b9de992aa3d23c2999121d735e53f9c'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_REALTlME'
        response=requests.post(url,headers=headers,data=data)
        print('response',response)
        target=response.json()
        print('html',target)
        ent2.insert(INSERT,target['translateResult'][0][0]['tgt'])
        ent2.insert(INSERT,'\n')
        
    #输入要翻译的内容
    root=Tk()
    root.title='小小翻译家'
    root.resizable(width=False,height=False)
    root.configure(bg='skyblue')
    Label(root, text='请输入翻译内容：', bg='skyblue', font=('迷你简毡笔黑', 15)).grid(row=0, column=0)
    menubar=Menu(root,tearoff=False)
    ent=Text(root,width=40,height=8,bg='deepskyblue')
    ent.bind('<Button-3>',lambda x:rightKey(x,ent)) #绑定右键鼠标
    ent.configure(font=("迷你简毡笔黑"))
    ent.grid(row=0,column=1,padx=10,pady=5)

    #输出翻译结果
    Label(root, text='翻译结果：', bg='skyblue', font=('迷你简毡笔黑', 15)).grid(row=100, column=0)
    ent2 = Text(root, width=40, height=8, bg='deepskyblue')
    ent2.bind("<Button-3>", lambda x: rightKey(x, ent2))  # 绑定右键鼠标
    ent2.configure(font=("kust.ttf"))
    ent2.grid(row=100, column=1, padx=10, pady=5)

    button_clear=Button(root,text='清空',activebackground='aqua',
                        relief=FLAT,activeforeground='steelblue',
                        bg='steelblue',fg = "aqua",font=('迷你简毡笔黑',10),command=C)
    button_clear.grid(row=3,column=1,sticky=E,padx=10,pady=5)

    button_fanyi=Button(root,text='点击翻译',activeforeground='aqua',relief=FLAT,activebackground='steelblue',bg = "steelblue",fg = "aqua",font=('迷你简毡笔黑',10),command=youdao)
    button_fanyi.grid(row=4,column=1,sticky=E,padx=10,pady=5)
    mainloop()