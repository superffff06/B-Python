import math
import time
import sys
import random
import os
import shutil
import functools
import operator
import threading
from tkinter import *
from multiprocessing import Process,cpu_count
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
from PIL import Image,ImageTk
from clock_creation import create_clock
from calc_creation import create_calc
from tictac_creation import create_tictac
from snake_creation import create_snake
from variables import xx,yy

def create_clock1():
    create_clock()
def create_calc1():
    create_calc()
def create_tictac1():
    create_tictac()
def create_snake1():
    create_snake()
window=Tk()
clock_image_org = Image.open("clock.png")
clock_sizeH=70
clock_sizeW=70
clock_image_org = clock_image_org.resize((clock_sizeH,clock_sizeW))
clock_image = ImageTk.PhotoImage(master = window,image = clock_image_org)
calc_image_org = Image.open("calculator.png")
calc_sizeH=70
calc_sizeW=70
calc_image_org =calc_image_org.resize((calc_sizeH,calc_sizeW))
calc_image = ImageTk.PhotoImage(master = window,image = calc_image_org)
tictac_image_org = Image.open("ttt.png")
tictac_sizeH=70
tictac_sizeW=70
tictac_image_org =tictac_image_org.resize((tictac_sizeH,tictac_sizeW))
tictac_image = ImageTk.PhotoImage(master = window,image = tictac_image_org)
snake_image_org = Image.open("sarpe.png")
snake_sizeH=70
snake_sizeW=70
snake_image_org = snake_image_org.resize((snake_sizeH,snake_sizeW))
snake_image = ImageTk.PhotoImage(master = window,image = snake_image_org)
window.geometry("500x500")
window.title("Easy-App")
window.configure(bg="#d1cbba")
button_clock = Button(window,
                height=clock_sizeH+30,
                width=clock_sizeW,
                bg="#75b40f",
                fg="black",
                text="Clock",
                image=clock_image,
                command=create_clock1,
                compound=TOP)
button_clock.grid(row = 0, column = 0)
button_calc = Button(window,
                height=calc_sizeH+30,
                width=calc_sizeW,
                bg="#3c85fa",
                fg="black",
                text="Calculator",
                image=calc_image,
                command=create_calc,
                compound=TOP)
button_calc.grid(row = 0, column = 1)
button_tictac = Button(window,
                height=tictac_sizeH+30,
                width=tictac_sizeW,
                bg="red",
                fg="black",
                text="TicTacToe",
                image=tictac_image,
                command=create_tictac1,
                compound=TOP)
button_tictac.grid(row = 0, column = 2)
button_snake = Button(window,
                height=snake_sizeH+30,
                width=snake_sizeW,
                bg="#821e9e",
                fg="black",
                text="Snake",
                image=snake_image,
                command=create_snake1,
                compound=TOP)
button_snake.grid(row = 0, column = 3)
window.mainloop()