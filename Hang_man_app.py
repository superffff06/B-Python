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
from nltk.corpus import words

def end_the_game():
    global end_game_window
    global main_window
    end_game_window.destroy()
    main_window.destroy()
def restart_game():
    global end_game_window
    if end_game_window is not None and end_game_window.winfo_exists():
        end_game_window.destroy() 
        end_game_window = None
    global human_label
    if human_label is not None and human_label.winfo_exists():
       human_label.destroy()
       human_label = None
    global hangman_label
    if hangman_label is not None and hangman_label.winfo_exists():
       hangman_label.destroy()
       hangman_label = None
    global letters_used
    if letters_used is not None and letters_used.winfo_exists():
       letters_used.destroy()
       letters_used = None
    global word_canvas
    if word_canvas is not None and word_canvas.winfo_exists():
       word_canvas.destroy()
       word_canvas = None
    global enter_word_label
    if enter_word_label is not None and enter_word_label.winfo_exists():
        enter_word_label.destroy()
        enter_word_label = None
    global enter_guess_letter
    if enter_guess_letter is not None and enter_guess_letter.winfo_exists():
        enter_guess_letter.destroy()
        enter_guess_letter = None
    global used_letters
    used_letters = ""
    global entry_label
    entry_label = Label(main_window,
                    text="Please select the 2 player option or the 1 player option",
                    fg="red",
                    font=("Arial",15),
                    bg="#000000"
                    )
    entry_label.place(x = 0,y = 50)
    global B2player_button
    B2player_button = Button(main_window,
                        text="2 Player gamemode",
                        font=("Arial", 15),
                        bg="green",
                        fg="red",
                        command=gamemode2 )
    global B1player_button
    B1player_button = Button(main_window,
                        text="1 Player gamemode",
                        font=("Arial", 15),
                        bg="green",
                        fg="red",
                        command=gamemode1 )
    B2player_button.place( x = 292, y = 79)
    B1player_button.place( x = 0, y = 79)
def delete_widgets():
    global entry_label,B2player_button, B1player_button
    entry_label.destroy()
    B2player_button.destroy()
    B1player_button.destroy()
def gameover(win_or_not):
    global hangman_word
    global end_game_window
    end_game_window = Toplevel(main_window)
    end_game_window.geometry("500x500")
    if win_or_not:
        end_text = "You won! The word was: " + hangman_word
    else:
        end_text = "You lost! The word was: " + hangman_word
    end_message = Label(end_game_window,
                        text = end_text + "\n" + "Would you like to play again or quit ? " ,
                        font = ("Arial" , 15),
                        anchor = "w")
    end_message.place(x=0, y=100)
    play_again_button = Button(end_game_window,
                               text="Play again",
                               font=("Arial", 15),
                               bg = "green",
                               fg = "red",
                               command = restart_game)
    quit_button = Button(end_game_window,
                         text="Quit",
                         font=("Arial", 15),
                         bg = "green",
                         fg = "red",
                         command = end_the_game)
    play_again_button.place(x=0, y=180)
    quit_button.place(x=270, y=180)
def true_gamemode():
    global reaper_image_org, reaper_image , human_image_org, human_image
    reaper_image_org = Image.open("reaper-death.png")
    human_image_org = Image.open("scared_human.png")
    reaper_image_sizeH = 100
    reaper_image_sizeW = 100
    human_image_sizeH = 100
    human_image_sizeW = 100
    reaper_image_org = reaper_image_org.resize((reaper_image_sizeH, reaper_image_sizeW))
    human_image_org = human_image_org.resize((human_image_sizeH, human_image_sizeW))
    reaper_image = ImageTk.PhotoImage(master = main_window, image = reaper_image_org)
    human_image = ImageTk.PhotoImage(master = main_window, image = human_image_org)
    global hangman_word
    global hangman_label
    global used_letters
    global distance_images
    global guessed_letters
    global human_label
    delete_widgets()
    global death_counter, death_maxim
    death_counter = int(0)
    death_maxim = int(10)
    guessed_letters = 0
    word_length = len(hangman_word)
    global word_canvas
    word_canvas = Canvas(main_window,
                         bg="grey",
                         )
    hangman_label = Label(main_window,
                            height = reaper_image_sizeH+30,
                            width = reaper_image_sizeW,
                            image = reaper_image)
    human_label = Label(main_window,
                        height = human_image_sizeH+30,
                        width = human_image_sizeW,
                        image = human_image)
    hangman_label.place(x=0, y=0)
    human_label.place(x=600, y=0)
    word_canvas_width = 700
    word_canvas.place(x=0, y=500, width=word_canvas_width, height=50)
    distance_images = word_canvas_width - reaper_image_sizeW - human_image_sizeW
    line_length = 680 / word_length
    sx = 0
    line_ids = []
    for i in  range(0,word_length):
        lx = sx+line_length
        line_id = word_canvas.create_line(sx+8 , 
                                40, 
                                lx, 
                                40, 
                                fill="purple", 
                                width = 2
                                )
        line_ids.append(line_id)
        sx = lx
    global enter_word_label
    enter_word_label = Label(main_window,
                             text = "Type a letter to see if it is in the word",
                             font = ("Arial", 15)
                             )
    global enter_guess_letter
    enter_guess_letter = Entry(main_window,
                               font = ("Arial", 15)
                               )
    guessed_letters_label = Label(main_window,
                                  )
    enter_word_label.place(x=0 , y = 380)
    enter_guess_letter.place(x = 140 , y = 410 , width = 30)
    strletters_used = StringVar()
    strletters_used.set("Used letters : ")
    global letters_used
    letters_used = Label(main_window,
                         textvariable = strletters_used,
                         font = ("Arial", 10),
                         fg = "white",
                         bg = "black",
                         width = 40,
                         height = 2,
                         anchor = "w"
                         )
    letters_used.place(x=0, y=290)
    def on_enter(event):
        global reaper_image_org, reaper_image , human_image_org, human_image
        global death_counter
        global death_maxim
        global hangman_label
        global used_letters
        global distance_images
        global guessed_letters
        guess = enter_guess_letter.get()
        if len(guess)==0 or len(guess)>1 or guess.isalpha()==False or (guess in used_letters ):
            messagebox.showerror("Error", "Please enter a single unused letter")
            enter_guess_letter.delete(0,END)
            return 
        else:
            number_of_correct_letters = 0
            for i in hangman_word:
                if i == guess:
                    number_of_correct_letters = number_of_correct_letters + 1
            if number_of_correct_letters == 0:
                if used_letters =="":
                    used_letters = guess
                else :
                    used_letters = used_letters + ", " + guess
                strletters_used.set ("Used letters : " + used_letters)
                death_counter = death_counter + 1
                info = hangman_label.place_info()
                current_x = float(info["x"])
                current_y = float(info["y"])
                changingx = float(distance_images/(death_maxim-1))
                newx = current_x+changingx
                hangman_label.place_configure(x = newx,y = current_y)
                if death_counter == death_maxim:
                    line_ids.clear()
                    gameover(False)
            if number_of_correct_letters > 0 :
                letter_id = 0
                for i in hangman_word:
                    if i == guess and line_ids[letter_id] is not None:
                       guessed_letters = guessed_letters  + 1
                       coords = word_canvas.coords(line_ids[letter_id])
                       word_canvas.delete(line_ids[letter_id])
                       line_ids[letter_id]= None
                       word_canvas.create_text(coords[0]+line_length/2, 
                                               coords[1] - 10, 
                                               text = guess,
                                               font = ("Arial", 20),
                                               width = line_length/2,
                                               fill = "black"
                                               )
                      
                    letter_id = letter_id + 1
                if guessed_letters == word_length:
                    line_ids.clear()
                    gameover(True)
            enter_guess_letter.delete(0,END)

    enter_guess_letter.bind("<Return>", on_enter)
def on_enter(event):
    hangman_word = word_entry.get()
    new_window.destroy()

def gamemode2 ():
    global hangman_word
    new_window = Toplevel(main_window)
    new_window.geometry("500x500");
    new_window.title("Please enter a word")
    do_not_look = Label(new_window,
                        text="Make sure the other player does not see your word",
                        font=("Arial", 15) )
    do_not_look.place(x=20, y=70)
    word_entry = Entry(new_window,
                       font=("Arial", 15),
                       )
    def on_enter(event):
        global hangman_word
        if(word_entry.get().isalpha()):
           hangman_word = word_entry.get()
           new_window.destroy()
           true_gamemode()
        else :
            messagebox.showerror("Error", "Please use only letters in the word")
    word_entry.bind("<Return>", on_enter)
    word_entry.place(x=100, y=100)
def gamemode1():
    global hangman_word
    hangman_word = random.choice(word_list).lower()
    true_gamemode()

main_window =Tk()
global death_counter
global used_letters
global death_maxim
global hangman_word
global word_entry
global B2player_button
global B1player_button
global hangman_label
global distance_images
global reaper_image_org, reaper_image , human_image_org, human_image
global guessed_letters
global end_game_window
global human_label
global letters_used
global word_canvas
global enter_word_label
global enter_guess_letter
global entry_label
global B1player_button
global B2player_button
global word_list
word_list = words.words()
entry_label = None
death_counter = None
death_maxim = None
hangman_word = None
word_entry = None
B2player_button  = None
B1player_button = None
hangman_label = None
reaper_image_org = None
reaper_image = None
human_image_org = None
human_image = None
guessed_letters = None
end_game_window = None
human_label = None
letters_used = None
word_canvas = None
enter_word_label = None
enter_guess_letter = None
main_window.geometry("700x700")
restart_game()
main_window.mainloop()