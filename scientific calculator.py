from tkinter import *
import math
root=Tk()
root.title("scientific calculator")

e=Entry(root,width=30,borderwidth=5)
e.grid(row=0, column=0,padx=10,pady=10,columnspan=2)
root.geometry("711x358")
h="("
g=")"

def resize():
    root.geometry("1187x358")
def click(number):
    x=e.get()
    e.delete(0, 'end')
    e.insert(0,str(x)+str(number))
def add():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "addition"
        firnum = float(x)
        e.delete(0, 'end')
    else:
        math1 = "addition"
        firnum = float(fnum)
        e.delete(0, 'end')

def multiply():
    fnum = e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "multiplication"
        firnum = float(x)
        e.delete(0, 'end')
    else:
        math1 = "multiplication"
        firnum = float(fnum)
        e.delete(0, 'end')
def subtract():
    fnum = e.get()
    global firnum
    global math1
    if h and g in fnum:
        x = fnum[1]
        math1 = "subtraction"
        firnum = float(x)
        e.delete(0, 'end')
    else:
        math1 = "subtraction"
        firnum = float(fnum)
        e.delete(0, 'end')

def division():
    fnum = e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "division"
        firnum = float(x)
        e.delete(0, 'end')
    else:
        math1="division"
        firnum = float(fnum)
        e.delete(0, 'end')
def par1():
    fnum=e.get()
    global firnum
    global math1
    math1="parenthesis1"
    firnum=str(fnum)
    e.insert(0, '(')
    e.insert('end',')')


def dot():
    fnum=e.get()
    global math1
    global firnum
    math1="decimals"
    firnum=int(fnum)
    e.delete(0, 'end')
    e.insert(0,str(firnum)+".")
def x2():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "square"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,int(firnum)**3)
    else:
        math1="square"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, int(firnum) ** 2)
def x3():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "cube"
        firnum = float(x)
        e.insert(0,int(firnum)**3)
    else:
        math1="cube"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, int(firnum) ** 3)
def ex():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "epowerx"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,math.exp(firnum))
    else:

        math1="epowerx"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, math.exp(firnum))
def log10():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "log10"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,math.log10(firnum))
    else:

        math1="log10"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, math.log10(firnum))
def byx():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "1byx"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,1/float(firnum))
    else:

        math1="1byx"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, 1 / float(firnum))
def sqrootx():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "sqroot"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,math.sqrt(firnum))
    else:

        math1="sqroot"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, math.sqrt(firnum))
def curootx():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "cuberoot"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,float(firnum)**(1/3))
    else:

        math1="cuberoot"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, float(firnum) ** (1 / 3))
def tenx():
    fnum = e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "tenx"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,10**float(firnum))
    else:

        math1 = "tenx"
        firnum = float(fnum)
        e.delete(0, 'end')
        e.insert(0, 10 ** float(firnum))
def xfact():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "xfact"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,math.factorial(int(firnum)))
    else:

        math1="xfact"
        firnum=int(fnum)
        e.delete(0, 'end')
        e.insert(0, math.factorial(int(firnum)))
def ee():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "ee"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,float(firnum)*2.718281828459045)
    else:

        math1="ee"
        firnum=str(fnum)
        enum = str(firnum)
        if len(e.get()) == 0:
            firnum = str(fnum)
            e.insert(0, 1 * 2.718281828459045)
        else:
            e.insert(0, float(firnum) * 2.718281828459045)
def ln():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "ln"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0,math.log(firnum))
    else:

        math1="ln"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, math.log(firnum))
def xy():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x=fnum[1]
        math1 = "xy"
        firnum = float(x)
        e.delete(0, 'end')

    else:
        math1 = "xy"
        firnum = float(fnum)
        e.delete(0, 'end')



def pi():
    fnum=e.get()
    global firnum
    global math1

    if h and g in fnum:
        x=fnum[1]
        math1 = "pi"
        firnum = float(x)
        e.delete(0, 'end')
        if len(e.get())<=0:
            e.insert(0, float(firnum) * 3.141592653589793)
    else:
        firnum = str(fnum)
        pinum = e.get()
        math1="pi"
        if len(e.get()) == 0:
            firnum = str(fnum)
            e.insert(0, 1 * 3.141592653589793)
        else:
            e.insert(0, float(firnum) * 3.141592653589793)

def sin():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x = fnum[1]
        math1 = "sin"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0, math.sin(firnum))
    else:
        math1 = "sin"
        firnum = float(fnum)
        e.delete(0, 'end')
        e.insert(0, math.sin(firnum))


def cos():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x = fnum[1]
        math1 = "cos"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0, math.cos(firnum))
    else:

        math1="cos"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, math.cos(firnum))
def tan():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x = fnum[1]
        math1 = "tan"
        firnum = float(x)
        e.delete(0, 'end')
        e.insert(0, math.tan(firnum))
    else:

        math1="tan"
        firnum=float(fnum)
        e.delete(0, 'end')
        e.insert(0, math.tan(firnum))
def yrootx():
    fnum=e.get()
    global firnum
    global math1
    if h and g in fnum:
        x = fnum[1]
        math1 = "rootx"
        firnum = float(x)
        e.delete(0, 'end')

    else:

        math1="rootx"
        firnum=float(fnum)
        e.delete(0, 'end')
def integer():
    fnum=e.get()
    global math1
    global firnum
    if h and g in fnum:
        x = fnum[1]
        math1 = "integer"
        firnum = float(x)
        e.insert(0, "-"+ str(firnum))
        e.delete(0, 'end')
    else:

        math1 = "integer"
        firnum=-float(fnum)
        e.insert(0, "-"+ str(firnum))
        e.delete(0, 'end')




def equalto():
    if math1=="addition":
        snum = e.get()
        e.delete(0, 'end')
        e.insert(0, firnum + float(snum))


    elif math1=="subtraction":

        sunum = e.get()
        e.delete(0, 'end')
        e.insert(0, firnum - float(sunum))
    elif math1=="multiplication":
        mnum = e.get()
        e.delete(0, 'end')
        e.insert(0, firnum * float(mnum))
    elif math1=="division":
        dnum = e.get()
        e.delete(0, 'end')
        e.insert(0, firnum/ float(dnum))
    elif math1=="parenthesis1":
        par1()
        equalto()
    elif math1=="decimals":
        dot()

    elif math1=="square":
        x2()
    elif math1=="cube":
        x3()
    elif math1=="epowerx":
        ex()
    elif math1=="log10":
        log10()
    elif math1=="1byx":
        byx()
    elif math1=="sqroot":
        sqrootx()
    elif math1=="cuberoot":
        curootx()
    elif math1=="tenx":
        tenx()
    elif math1=="xfact":
        xfact()

    elif math1=="ln":
        ln()

    elif math1=="xy":
        xynum = e.get()
        e.delete(0, 'end')
        e.insert(0, firnum ** (float(xynum)))
    elif math1=="sin":
        sin()

    elif math1=="cos":
        cos()

    elif math1=="tan":
        tan()

    elif math1=="rootx":
        yroox=e.get()
        e.delete(0,'end')
        e.insert(0, firnum ** (1 / float(yroox)))
    elif math1=="integer":
        integer()

def clearall():
    e.delete(0,'end')

b1=Button(root,text=1,padx=80,pady=20,command=lambda:click(1))
b2=Button(root,text=2,padx=80,pady=20,command=lambda:click(2))
b3=Button(root,text=3,padx=80,pady=20,command=lambda:click(3))
b4=Button(root,text=4,padx=80,pady=20,command=lambda:click(4))
b5=Button(root,text=5,padx=80,pady=20,command=lambda:click(5))
b6=Button(root,text=6,padx=80,pady=20,command=lambda:click(6))
b7=Button(root,text=7,padx=80,pady=20,command=lambda:click(7))
b8=Button(root,text=8,padx=80,pady=20,command=lambda:click(8))
b9=Button(root,text=9,padx=80,pady=20,command=lambda:click(9))
b0=Button(root,text=0,padx=80,pady=20,command=lambda:click(0))
badd=Button(root,text="+",padx=80,pady=20,command=lambda:add())
bequal=Button(root,text="=",padx=80,pady=20,command=lambda:equalto())
bclear=Button(root,text="clear",padx=70,pady=20,command=lambda:clearall())
bdiv=Button(root,text="/",padx=80,pady=20,command=lambda:division())
bmultiply=Button(root,text="x",padx=80,pady=20,command=lambda:multiply())
bsub=Button(root,text="-",padx=80,pady=20,command=lambda:subtract())
bsci=Button(root,text="scientific calculator",padx=20,pady=20,command=lambda:resize())
bpar1=Button(root,text="()",padx=80,pady=20,command=lambda:par1())
bdot=Button(root,text=".",padx=81,pady=20,command=lambda:dot())
bx2=Button(root,text="x\u00B2",padx=50,pady=20,command=lambda:x2())
bx3=Button(root,text="x\u00B3",padx=50,pady=20,command=lambda:x3())
bex=Button(root,text="e\u02E3",padx=50,pady=20,command=lambda:ex())
blog10=Button(root,text="log\u2081\u2080",padx=40,pady=20,command=lambda:log10())
b1x=Button(root,text="1/x",padx=75,pady=20,command=lambda:byx())
b2rootx=Button(root,text=u'\u221A'+"x",padx=45,pady=20,command=lambda:sqrootx())
b3rootx=Button(root,text=u'\u221B'+"x",padx=45,pady=20,command=lambda:curootx())
b10x=Button(root,text="10\u02E3",padx=43,pady=20,command=lambda:tenx())
bxfact=Button(root,text="x!",padx=50,pady=20,command=lambda:xfact())
bee=Button(root,text="e",padx=50,pady=20,command=lambda:ee())
bln=Button(root,text="ln",padx=50,pady=20,command=lambda:ln())
bxy=Button(root,text="x\u02B8",padx=50,pady=20,command=lambda:xy())
bpi=Button(root,text="\u220F",padx=50,pady=20,command=lambda:pi())
bsin=Button(root,text="sin()",padx=40,pady=20,command=lambda:sin())
bcos=Button(root,text="cos()",padx=40,pady=20,command=lambda:cos())
btan=Button(root,text="tan()",padx=40,pady=20,command=lambda:tan())
byrootx=Button(root,text=u'\u02B8'+u'\u221A'+"x",padx=45,pady=20,command=lambda:yrootx())
binteger=Button(root,text=u'\u207A'+"/"+u'\u208B',padx=45,pady=20,command=lambda:integer())



b1.grid(row=3 ,column=0)
b2.grid(row=3 ,column=1 )
b3.grid(row=3 ,column=2 )
b4.grid(row=2,column=0)
b5.grid(row=2,column=1 )
b6.grid(row=2,column=2 )
b7.grid(row=1,column=0)
b8.grid(row=1,column=1 )
b9.grid(row=1,column=2)
b0.grid(row=4,column=0 )
badd.grid(row= 4,column=3)
bequal.grid(row=4,column=1)
bclear.grid(row=5,column=0)
bdiv.grid(row=1,column=3 )
bmultiply.grid(row=2 ,column=3 )
bsub.grid(row=3,column=3)
bsci.grid(row=5,column=1)

bpar1.grid(row=4,column=2)
bdot.grid(row=5,column=2)
bx2.grid(row=1,column=4)
bx3.grid(row=1,column=5)
bex.grid(row=1,column=6)

blog10.grid(row=2,column=4)
b1x.grid(row=5,column=3)
b2rootx.grid(row=2,column=6)
b3rootx.grid(row=2,column=7)
b10x.grid(row=1,column=7)

bxfact.grid(row=3,column=4)
bee.grid(row=3,column=5)
bln.grid(row=3,column=6)
bxy.grid(row=3,column=7)
bpi.grid(row=2,column=5)

bsin.grid(row=4,column=4)
bcos.grid(row=4,column=5)
btan.grid(row=4,column=6)
byrootx.grid(row=4,column=7)
binteger.grid(row=5,column=4)

root.mainloop()
