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

class Car:
    model = None
    year = None
    color = None
    speed = None
    wheels = 4
    def __init__(self,model) :
        self.model=model
    def Update_Speed (self,speed):
        self.speed=speed
    def Update_Year(self,year):
        self.year=year
    def Update_Color(self,color):
        self.color=color
    def Update_Model(self,model):
        self.model=model
    def drive(self):
        print("This car is driving with "+str(self.speed))
    def stop(self):
        print("This car has stopped")
class Mini_Car(Car):
    def __init__(self,model,speed):
        super().__init__(model)
        self.speed=speed
class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")
class Rabbit(Animal):
    alive = False
class Fish(Animal):
    pass
class Hawk(Animal):
    pass
class Thing(Animal,Car):
    pass

Barcelona =Car("Ferrari")
Barcelona.speed = 15
Barcelona.Update_Speed(16)
print (str(Barcelona.speed))
Madrid = Mini_Car("Lamborghini",15)
print (str(Madrid.model) + "\n" +  str(Madrid.speed))