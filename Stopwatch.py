# ---------------------------------------------------------------  imports

from tkinter import *
import tkinter as tk
import time
# --------------------------------------------------------------- Variables

hr = 00
min = 00
sec = 00
text_format = (hr , ":", min, ":", sec)
yes = True
colour_change = True

# --------------------------------------------------------------- Function for updating time format


def update():
    global min, hr, sec

    if sec == 59:
        min += 1
        sec = 0
    if min == 59:
        hr += 1
        min = 0

# --------------------------------------------------------------- Function for making time work


def time_work():
    global sec, text_format
    if yes:
        sec += 1
        text_format = (hr, ":", min, ":", sec)
        my_label.config(text = text_format)
        update()
        start()


# ---------------------------------------------------------------  main tkinter
xpo = tk.Tk()
xpo.title("Stopwatch")

# ---------------------------------------------------------------  our text display

my_label = tk.Label(

    bg = "#a6a6a6",
    width = 18,
    # height = 5,
    text = (text_format),
    font = ("Agency FB", 35),

)

my_label.pack(pady = (20, 0))

# --------------------------------------------------------------- My button label

my_btn_label = tk.Label(



)

my_btn_label.pack(pady = 20)

# --------------------------------------------------------------- Function for start button


def start():
    global yes, colour_change
    yes = True
    my_start.config(state=DISABLED)
    my_start.config(bg = "SystemButtonFace")
    colour_change = False
    xpo.after(990, time_work)

# --------------------------------------------------------------- Function for start button


def stop():
    global yes, colour_change
    yes = False
    colour_change = True
    my_start.config(state = NORMAL)
    my_start.config(bg="lime")

# --------------------------------------------------------------- My start button


my_start = tk.Button(
    my_btn_label,
    bd = 0,
    text = "Start",
    bg = "lime",
    width = 20,
    command = start,
)

my_start.grid(row = 0, column = 0, padx = 10, )


# ---------------- Binding for the start button


def start_enter(x):
    if colour_change:
        my_start.config(bg="Green")


def start_leave(x):
    if colour_change:
        my_start.config(bg="Lime")


my_start.bind("<Enter>", start_enter)
my_start.bind("<Leave>", start_leave)

# --------------------------------------------------------------- My stop button

my_stop = tk.Button(
    my_btn_label,
    bd = 0,
    text = "Stop",
    width = 20,
    bg="#E74C3C",
    command = stop,

)

my_stop.grid(row = 0, column = 1, padx = 10,)


# ---------------- Binding for the stop button


def stop_enter(x):
    my_stop.config(bg="red")


def stop_leave(x):
    my_stop.config(bg="#E74C3C")


my_stop.bind("<Enter>", stop_enter)
my_stop.bind("<Leave>", stop_leave)

# ---------------------------------------------------------------  tkinter loop
xpo.mainloop()

"""xpo.resizable(0,0)
xpo.title("Digital Clock")
xpo.config(bg = "white")


def start():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    am_pm = time.strftime("%p")
    second = time.strftime("%S")
    day = time.strftime("%A")

    l1.config(text = hour + ":" + minute + ":" + second + ":" + am_pm)
    l2.config(text = day)
    l1.after(500, start)


l1 = tk.Label(xpo, width = 10, bg = "white", fg = "lime", font = ( "Agency FB", 50))
l1.pack(pady = 10, padx = 20)

l2 = tk.Label(xpo, bg = "white", fg = "lime", font = ( "Agency FB", 20))
l2.pack(pady = (0, 10))

start()"""