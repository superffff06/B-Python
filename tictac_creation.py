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

def next_turn(row,column):
    global ttplayer
    global ttplayers
    global ttbuttons
    global ttlabel
    global ttwindow
    if ttbuttons[row][column]["text"] == ""  and check_winner()==False :
        if ttplayer == ttplayers[0]:
            ttbuttons[row][column]["text"]=ttplayer
            if check_winner() == False:
                ttplayer=ttplayers[1]
            elif check_winner() == True:
                ttlabel.config(text=ttplayers[0] + " wins")
                return True
            elif check_winner() == "Tie":
                ttlabel.config(text="Tie")
                return True 
        else :
           ttbuttons[row][column]["text"]=ttplayer
           if check_winner() == False:
                ttplayer=ttplayers[0]
           elif check_winner() == True:
                ttlabel.config(text=ttplayers[1] + " wins")
                return True
           elif check_winner() == "Tie":
                ttlabel.config(text="Tie")
                return True
        ttlabel.config(text=ttplayer +"'s turn")

def check_winner():
    global ttbuttons
    for row in range(3):
        if ttbuttons[row][0]["text"]==ttbuttons[row][1]["text"] and ttbuttons[row][0]["text"]==ttbuttons[row][2]["text"] and ttbuttons[row][0]["text"]!="":
            return True
        if ttbuttons[0][row]["text"]==ttbuttons[1][row]["text"] and ttbuttons[1][row]["text"]==ttbuttons[2][row]["text"] and ttbuttons[0][row]["text"]!="":
            return True
    if ttbuttons[0][0]["text"]==ttbuttons[1][1]["text"] and ttbuttons[1][1]["text"]==ttbuttons[2][2]["text"] and ttbuttons[0][0]["text"]!="":
        return True
    if ttbuttons[0][2]["text"]==ttbuttons[1][1]["text"] and ttbuttons[1][1]["text"]==ttbuttons[2][0]["text"] and ttbuttons[0][2]["text"]!="":
        return True
    if empty_spaces()==False:
        return "Tie"
    return False
def empty_spaces():
    nr=0
    global ttbuttons
    for row in range(3):
        for column in range(3):
            if ttbuttons[row][column]["text"]=="":
                nr=nr+1
    if nr==0:
        return False
    else :
        return True
def new_game():
    global ttbuttons
    global ttplayers
    global ttplayer
    for row in range(3):
        for column in range(3):
            ttbuttons[row][column]["text"]=""
    ttplayer=random.choice(ttplayers)
    ttlabel.config(text=ttplayer + "'s turn")
    
def create_tictac():
    global ttwindow
    ttwindow=Tk()
    ttwindow.resizable(False,False)
    ttwindow.title("TicTacToe")
    ttwindow.geometry("600x600")
    global ttplayers
    ttplayers=["x","o"]  
    global ttplayer
    ttplayer=random.choice(ttplayers)
    global ttbuttons
    ttbuttons = [[0,0,0],[0,0,0],[0,0,0]]
    global ttlabel
    ttlabel=Label(ttwindow,
                  text= ttplayer +"'s turn",
                  font=("consolas",20),
                  fg="black",
                  bg="red")
    ttlabel.pack()
    reset_button=Button(ttwindow,
                  text="Restart",
                  font=("consolas",20),
                  command=new_game,
                  fg="black",
                  bg="red")
    reset_button.pack()
    ttframe=Frame(ttwindow)
    ttframe.pack()
    for row in range(3):
        for column in range(3):
            ttbuttons[row][column]= Button(ttframe,
                                           text="",
                                            font=("consolas",20),
                                            width=7,
                                            height=4,
                                            bg="grey",
                                            fg="red",
                                            activebackground="grey",
                                            command= lambda rowtt=row,columntt=column : next_turn(rowtt,columntt))
            ttbuttons[row][column].grid(row=row,column=column)
    ttwindow.mainloop()