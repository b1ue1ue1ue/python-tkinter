from tkinter import *
app=Tk()

app.geometry('400x400')
app.wm_title('计算器')


button_txt=[
    ['7','8','9','+'],
    ['4','5','6','-'],
    ['1','2','3','*'],
    ['(',')','0','/'],
    ['清空','退格','.','='],
]

display=StringVar()
def set_content(text):
    content=display.get()+text
    display.set(content)
def clr():
    display.set('')
def bck():
    display.set(str(display.get()[:-1]))
def cal():
    try:
        num=display.get()
        res=eval(num)
        display.set(num+'='+str(res))
    except:
        display.set('error!')

label=Label(app,textvariable=display,relief='ridge',font=('Arail','15'),anchor=E,text='')
label.place(x=0,y=0,width=400,height=60)


for i in range(5):
    for j in range(4):
        if button_txt[i][j]=='=':
            button=Button(
                app,
                text=button_txt[i][j],
                font=('Arial','14'),
                command=cal
            )
            button.place(x=100 * j, y=60 * i + 60, width=100, height=60)
        elif button_txt[i][j]=='清空':
            button=Button(
                app,
                text=button_txt[i][j],
                font=('Arial','14'),
                command=clr
            )
            button.place(x=100 * j, y=60 * i + 60, width=100, height=60)
        elif button_txt[i][j]=='退格':
            button=Button(
                app,
                text=button_txt[i][j],
                font=('Arial','14'),
                command=bck
            )
            button.place(x=100 * j, y=60 * i + 60, width=100, height=60)
        else:
            button=Button(
                app,
                text=button_txt[i][j],
                font=('Arial','14'),
                command=lambda text=button_txt[i][j]:set_content(text)
            )
            button.place(x=100 * j, y=60 * i + 60, width=100, height=60)





app.mainloop()