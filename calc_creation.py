import math
from time import *
import time
import sys
import random
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
 

def button_press(x):
     global equation_text
     equation_text = equation_text + str(x)
     equation_label.set(equation_text)
def clear_text():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)
def text_equal():
    global equation_text
    try :
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Error")
        equation_text="Error" 
    except SyntaxError:
        equation_label.set("Error")  
        equation_text="Error" 
def create_calc():
    global calc_window
    calc_window=Tk()
    calc_window.resizable(False,False)
    calc_window.title("Calc")
    calc_window.geometry("500x500")
    calc_window.configure(bg="#3b7e70")
    global equation_text
    equation_text = ""
    global equation_label
    equation_label = StringVar(calc_window)
    global calc_label
    global calc_frame
    bheight=2
    bwidth=5
    calc_frame=Frame(calc_window)
    calc_frame.place(x=130,y=100)
    calc_label = Label(calc_window,
                       textvariable=equation_label,
                       font=("consolas",11),
                       bg="white",
                       fg="black",
                       width=32,
                       height=4) 
    calc_label.place(x=130,y=20)
    button1=Button(calc_frame,
            text=1,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(1))
    button1.grid(row = 0, column = 0)
    button2=Button(calc_frame,
            text=2,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(2))
    button2.grid(row = 0, column = 1)
    button3=Button(calc_frame,
            text=3,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(3))
    button3.grid(row = 0, column = 2)
    button4=Button(calc_frame,
            text=4,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(4))
    button4.grid(row = 1, column = 0)
    button5=Button(calc_frame,
            text=5,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(5))
    button5.grid(row = 1, column = 1)
    button6=Button(calc_frame,
            text=6,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(6))
    button6.grid(row = 1, column = 2)
    button7=Button(calc_frame,
            text=7,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(7))
    button7.grid(row = 2, column = 0)
    button8=Button(calc_frame,
            text=8,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(8))
    button8.grid(row = 2, column = 1)
    button9=Button(calc_frame,
            text=9,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(9))
    button9.grid(row = 2, column = 2 )
    button0=Button(calc_frame,
            text=0,
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(0))
    button0.grid(row = 3, column = 1)
    button_plus=Button(calc_frame,
            text="+",
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press("+"))
    button_plus.grid(row = 3, column = 0)
    button_minus=Button(calc_frame,
            text="-",
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press("-"))
    button_minus.grid(row = 3, column = 2)
    button_multiply=Button(calc_frame,
            text="*",
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press("*"))
    button_multiply.grid(row = 0, column = 3)
    button_divide=Button(calc_frame,
            text="/",
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press("/"))
    button_divide.grid(row = 1, column = 3)
    button_equal=Button(calc_frame,
            text="=",
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command=text_equal)
    button_equal.grid(row = 2, column = 3)
    button_clear=Button(calc_frame,
            text="clear",
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command = clear_text)
    button_clear.grid(row = 3, column = 3)
    button_decimal=Button(calc_frame,
            text=".",
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press("."))
    button_decimal.grid(row = 4, column = 0)
    button_lp=Button(calc_frame,
            text="(",
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press("("))
    button_lp.grid(row = 4, column = 1)
    button_rp=Button(calc_frame,
            text=")",
            height=bheight,
            width=bwidth,
            font=("Arial",15),
            command= lambda : button_press(")"))
    button_rp.grid(row = 4, column = 2)
    button_fill=Button(calc_frame,
            bg="red",
            activebackground="red",
            height=bheight,
            width=bwidth)
    button_fill.grid(row = 4, column = 3)
    calc_window.mainloop()
create_calc()