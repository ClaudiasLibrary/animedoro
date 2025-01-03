from tkinter import *
from tkinter.ttk import Label
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#9B86BD"
BLUE2 = "#7776B3"
BLUE = "#5A639C"
PURPLE = "#E2BBE9"
FONT_NAME = "Courier"
WORK_MIN = 40
SHORT_BREAK_MIN = 20
LONG_BREAK_MIN = 20
REPS = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Bonus Episode!", foreground=BLUE2)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Episode!", foreground=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", foreground=BLUE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "🍡"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Animedoro")
window.config(padx=100, pady=50, bg=PURPLE)


title_label = Label(text="Timer", foreground=BLUE, background=PURPLE, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=PURPLE, highlightthickness=0)
heart_img = PhotoImage(file="heart.png")
canvas.create_image(100, 112, image=heart_img)
timer_text = canvas.create_text(100, 100, text = "00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(foreground=BLUE, background=PURPLE)
check_marks.grid(column=1, row=3)

window.mainloop()