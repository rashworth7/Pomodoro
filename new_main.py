from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_count = 1
timer_run = True
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer_run
    timer_run = False
    canvas.itemconfig(timer_text, text=f"25:00")
    label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global timer_run
    global timer_count
    timer_count += 1
    timer_run = True
    if timer_count > 7:
        countdown(LONG_BREAK_MIN * 60)
        label.config(text="Break", fg=RED)
    elif timer_count > 8:
        timer_run = False
        timer_count = 0
    elif timer_count % 2 == 0:
        countdown(WORK_MIN * 60)
        label.config(text="Work", fg=GREEN)
    else:
        countdown(SHORT_BREAK_MIN * 60)
        label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer_count
    if not timer_run:
        return
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        number_ticks = math.trunc(timer_count / 2)
        ticks = number_ticks * "✔"
        check_marks.config(text=ticks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

start = Button(text="Start", relief="raised", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", relief="raised", command=reset_timer)
reset.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()