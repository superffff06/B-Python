
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

def update_time():
     time_string = strftime("%I:%M:%S %p")
     time_label.config(text=time_string,
                       font=("Arial",30) )
     if clock_window.winfo_exists():
         time_label.after(1000,update_time)
     else :
          print("END")
          clock_window.destroy()
          clock_window.quit()
  

def create_clock():
     global clock_window
     clock_window=Tk()
     clock_window.resizable(False,False)
     clock_window.title("Clock")
     clock_window.geometry("500x500")
     clock_window.configure(bg="#d93d66")
     global time_label
     time_label = Label(clock_window,
                         font=("Arial",30),
                         bg="black",
                         fg="#09d3c0")
     time_label.place(x=180,y=100) 
     update_time()
     clock_window.mainloop()
