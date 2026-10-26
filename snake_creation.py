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

class Snake:
    body_size= None
    coordinates = []
    squares = []
    def __init__(self):
        self.body_size=body_parts
        self.coordinates.clear()
        self.squares.clear()
        for i in range(0,body_parts):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = snake_canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color, tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        xc=random.randint(0,int(game_width/space_size)-1) * space_size
        yc=random.randint(0,int(game_height/space_size)-1) * space_size
        self.coordinates = [xc,yc]
        snake_canvas.create_oval(xc,yc, xc+space_size, yc+space_size, fill=food_color, tag="foody")
def next_turn(food):
    global snake_window
    global snake_canvas
    global snake_label
    global direction
    global snake
    ok = 0
    snake_window.update()
    x=snake.coordinates[0][0]
    y=snake.coordinates[0][1]
    if direction == "up":
        y = y - space_size 
    elif direction == "down":
        y = y + space_size
    elif direction == "left":
        x = x - space_size
    elif direction == "right":
        x = x + space_size
    snake.coordinates.insert(0 , (x,y))
    square = snake_canvas.create_rectangle(x, y, x+space_size, y+space_size, fill=snake_color, tag="snake")
    snake.squares.insert(0,square)
    if x == food.coordinates[0] and y == food.coordinates[1] :
        global score
        score = score + 1
        snake_label.config(text="Score: " + str(score))
        snake_canvas.delete("foody")
        foodA = Food()
        snake_window.after(speed,next_turn, foodA)
    else :
        del snake.coordinates[-1]
        snake_canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        if check_collisions(snake) :
            game_over()
            direction = "down"
            snake = Snake()
            food = Food()
        snake_window.after(speed,next_turn, food)
def change_direction(new_direction):
    global direction
    global snake_window
    if new_direction == "left" :
        if direction !="right":
            direction= new_direction
    elif new_direction == "right" :
        if direction !="left":
            direction= new_direction
    elif new_direction == "up" :
        if direction !="down":
            direction= new_direction
    elif new_direction == "down" :
        if direction !="up":
            direction= new_direction
    snake_window.update()
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= game_width:
        return True
    if y < 0 or y >= game_height:
        return True
    for body_part in snake.coordinates[1:] :
        if x == body_part[0] and y == body_part[1] :
            return True
    return False
def game_over():
    global snake_canvas
    global snake_window
    global snake
    global score
    global food
    snake_canvas.delete('all')
    snake_window.update()
    snake_window_width=snake_canvas.winfo_width()
    snake_window_height=snake_canvas.winfo_height()
    snake_canvas.create_text(snake_window_width/2,snake_window_height/2,
                             font = ("consolas",50),
                             text="GAME OVER",
                             fill="red",
                             tag="gameover")
    score = 0
    snake_label.config(text="Score: " + str(score))
    snake_window.update()
    time.sleep(3)
    snake_window.update()
    for i in range(0,snake.body_size):
        snake.coordinates.pop(-1)
        snake.squares.pop(-1)
    del snake
    snake_canvas.delete('all')
def create_snake():
    global snake_window
    snake_window=Tk()
    snake_window.title("Snake")
    snake_window.config(background="#1859b5")
    snake_window.resizable(False,False)
    global game_width
    global game_height
    global speed
    global space_size
    global body_parts
    global snake_color
    global food_color
    global canvas_color
    global score
    global directions
    global direction
    global snake_label
    snake_color="#34eb4c"
    food_color="#d61a1a"
    canvas_color="#756c80"
    game_width=700
    game_height=650
    speed=150
    space_size=35
    body_parts=3
    score=0
    directions=["down","up","right","left"]
    direction="down"
    snake_label=Label(snake_window,
                      text="Score: " + str(score),
                      font=("consolas",30),
                      bg="#1859b5",
                      fg="red")
    snake_label.pack()
    global snake_canvas
    snake_canvas=Canvas(snake_window,
                        bg=canvas_color,
                        height=game_height,
                        width=game_width)
    snake_canvas.pack()
    snake_window.update()
    snake_window_width=snake_window.winfo_width()
    snake_window_height=snake_window.winfo_height()
    screen_width=snake_window.winfo_screenwidth()
    screen_height=snake_window.winfo_screenheight()
    x=int((screen_width/2)-(snake_window_width/2))
    y=int((screen_height/2)-(snake_window_height/2))
    snake_window.geometry(f"{snake_window_width}x{snake_window_height}+{x}+{y}")
    global snake
    global food
    snake = Snake()
    food = Food()
    snake_window.bind("<a>", lambda event: change_direction("left"))
    snake_window.bind("<d>", lambda event: change_direction("right"))
    snake_window.bind("<w>", lambda event: change_direction("up"))
    snake_window.bind("<s>", lambda event: change_direction("down"))
    next_turn(food)
    snake_window.mainloop()