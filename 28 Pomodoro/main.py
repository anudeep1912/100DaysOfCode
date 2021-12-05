from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK_MARK = "✔"
repetitions = 0
check_mark_count = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    global repetitions, check_mark_count
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    repetitions = 0
    check_mark_count = 1
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_start():
    global repetitions, check_mark_count
    repetitions += 1

    work_count = WORK_MIN * 60
    short_break_count = SHORT_BREAK_MIN * 60
    long_break_count = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:
        count_down(long_break_count)
        check_mark_count = 1
        timer_label.config(text="Break", fg=RED)
        window.attributes('-topmost', False)
    elif repetitions % 2 == 1:
        count_down(work_count)
        timer_label.config(text="Timer", fg=GREEN)
        checkmarks = TICK_MARK * check_mark_count
        check_mark.config(text=checkmarks)
        check_mark_count += 1
        window.attributes('-topmost', False)
    else:
        count_down(short_break_count)
        timer_label.config(text="Break", fg=PINK)
        window.attributes('-topmost', True)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
tomato_image = PhotoImage(file="tomato.png")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", command=timer_start)
start_button.grid(row=3, column=1)


reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=3, column=3)

timer_label = Label(text="Timer", font=(FONT_NAME, 60, "bold"))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(row=1, column=2)

check_mark = Label(font=(FONT_NAME, 20, "bold"))
check_mark.config(fg=GREEN, bg=YELLOW)
check_mark.grid(row=4, column=2)

window.mainloop()
