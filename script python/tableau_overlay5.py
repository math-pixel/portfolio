import tkinter
from tkinter import *
import tkinter.font
import turtle
#import mouse
#import keyboard
import time
#from pynput import keyboard


#fenetre 1
win = Tk()
win.attributes("-topmost", True )
win.overrideredirect(1)
win.attributes("-alpha",0.4)
#win.after(5000, lambda: win.focus_force())

#info
L = win.winfo_screenwidth()
H = win.winfo_screenheight()
#print (L,H)



def setup():
	t.hideturtle()
	t.up()
	

def enable_button():
        size_but = bouton1.winfo_height()
        global u
        #print(size_but)
        x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
        t.setpos(x - (win.winfo_screenwidth() / 2) ,(y * -1) + (win.winfo_screenheight() /2) + size_but + float(u))
        t.down()
        global i
        while i == True:
                #print(1)
                x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
                t.goto(x - (win.winfo_screenwidth() / 2) ,(y * -1) + (win.winfo_screenheight() /2) + size_but + float(u) )       
        setup()


def on_release(k):
        #print(k.widget)
        if str(k.widget) == ".!canvas":
                global i
                if i == True:
                        i = False
                else:
                        i = True
                        enable_button()
                
def focus(event):
        #print(str(event.widget))
        wid = win.focus_get() 
        #print(wid, "has focus")              

def clear_canvenas():
        t.clear()

def enable_window():
        global win_enable
        if win_enable == True:
                canvas.master.wm_attributes("-transparent", "white")
                win_enable = False
                bouton1.config(fg="#000000")
                bouton2.config(text = "stylo OFF", bg="red" , fg="#000000")
        else:
                canvas.master.wm_attributes("-transparent", "black")
                win_enable = True
                bouton1.config(fg="#ffffff")
                bouton2.config(text = "stylo ON", bg="green",fg="#ffffff")

def set_tortle_size(size):
        t.pensize(size)

def bleu():
        t.pencolor("blue")
        fbouton1.config(text="✔")
        fbouton2.config(text="")
        fbouton3.config(text="")
        fbouton4.config(text="")
def rouge():
        t.pencolor("red")
        fbouton1.config(text="")
        fbouton2.config(text="✔")
        fbouton3.config(text="")
        fbouton4.config(text="")
def vert():
        t.pencolor("green")
        fbouton1.config(text="")
        fbouton2.config(text="")
        fbouton3.config(text="✔")
        fbouton4.config(text="")
def noir():
        t.pencolor("white")
        fbouton1.config(text="")
        fbouton2.config(text="")
        fbouton3.config(text="")
        fbouton4.config(text="✔")

def leave():
        win.destroy()

def set_position_at_mouse(ecart):
        global u
        u = ecart

#widget de la fenetre  
#frame1
Frame1 = Frame(win,borderwidth=2,relief=GROOVE, bg='bisque')
Frame1.pack()

#frame -> button1,2,3,4....
font_button = tkinter.font.Font(size=26, weight="bold")
bouton1 = tkinter.Button(Frame1, width= 20,height=2, fg="#ffffff", bg="#1586f3", text="effacer le tableau",command=clear_canvenas)
bouton1.grid(row=0,column=2)
#2
bouton2 = tkinter.Button(Frame1, width= 20,height=2, fg="#ffffff", bg="green", text="stylo ON",command=enable_window)
bouton2.grid(row=0,column=3)
#3
bouton3 = tkinter.Button(Frame1, width= 20,height=2, fg="#ffffff", bg="#c70039", text="QUITTER",command=leave)
bouton3.grid(row=0,column=4)
#couleur
#62f11d
#d315f3

#frame2
Frame2 = Frame(Frame1,borderwidth=2,relief=GROOVE, bg='#62f11d')
Frame2.grid(row=0,column=1)

#frame2 --> button Color
fbouton1 = tkinter.Button(Frame2, width= 5,height=2, fg="#ffffff", bg="blue",command=bleu)
fbouton1.grid(row=0,column=1)
fbouton2 = tkinter.Button(Frame2, width= 5,height=2, fg="#ffffff", bg="red",command=rouge)
fbouton2.grid(row=0,column=2)
fbouton3 = tkinter.Button(Frame2, width= 5,height=2, fg="#ffffff", bg="green",command=vert)
fbouton3.grid(row=0,column=3)
fbouton4 = tkinter.Button(Frame2, width= 5,height=2, fg="#ffffff", bg="white",command=noir)
fbouton4.grid(row=0,column=4)
fbouton2.config(text="✔")

#frame3
Frame3 = Frame(Frame1,borderwidth=2,relief=GROOVE, bg='#B20BD4')
Frame3.grid(row=0,column=5)
#slider
slider = Scale(Frame3, from_=0, to=200,orient=HORIZONTAL,length=L/6, command=set_tortle_size,relief=GROOVE)
slider.grid(row=0,column=2)
slider.set(1)
#slider2
slider2 = Scale(Frame3, from_= 0, to=15,orient=HORIZONTAL,length=100, command=set_position_at_mouse,relief=GROOVE)
slider2.grid(row=0,column=4)
slider2.set(10)
#label
label = Label(Frame3, text= "taille :",bg='#B20BD4',fg="#ffffff")
label.grid(row=0,column=1)
#label2
label2 = Label(Frame3, text= "ecart souris:",bg='#B20BD4',fg="#ffffff", wraplength = 50)
label2.grid(row=0,column=3)

#canvas1
canvas = tkinter.Canvas(win, width=L, height=H ,bg="red")
canvas.master.overrideredirect(True)
canvas.pack()

#setting turtle
t = turtle.RawTurtle(canvas)
t.pencolor("red") # Red
t.speed(20)
t.pensize(1)

#declaration des variable
win_enable = True
i = False


setup()
win.bind("<Button-1>", on_release)
win.bind("<ButtonRelease-1>", on_release)

canvas.mainloop()


'''
#fenetre2
win2 = Tk()
win2.attributes("-alpha",0.0)
#win2.attributes("-topmost", True )
#canvas2
canvas2 = tkinter.Canvas(win2, width=L, height=H ,bg="white")
canvas2.master.overrideredirect(True)
#canvas.master.wm_attributes("-transparentcolor", "white")
canvas2.pack()

#win2.attributes("-topmost", True )

#win2.attributes("-topmost", True )

'''
