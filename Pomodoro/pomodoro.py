from tkinter import *
from tkinter import ttk
import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
ORANGE = "#ff944d"
LIGHT_ORANGE = "#ffe6b3"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
tick_index = 0
time_countdown = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global tick_index

    window.after_cancel(time_countdown)
    label_1.config(text= "Timer", foreground= ORANGE)
    label_2.config(text= "" * tick_index)
    canvas.itemconfig(timer, text= "00:00")
    reps = 1
    tick_index = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    playsound.playsound(r"Pomodoro\Assets\beep.mp3")
    if reps % 8 == 0: 
        label_1.config(text= "REST~", foreground= ORANGE)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0: 
        label_1.config(text= "Rest~", foreground= ORANGE)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        label_1.config(text= "Focus!", foreground= "red")
        countdown(WORK_MIN * 60)  

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(seconds):
    global time_countdown
    global reps
    global tick_index

    minutes = seconds // 60
    seconds_remaining = seconds % 60
    if seconds_remaining <= 9:
        seconds_remaining = f"0{seconds_remaining}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds_remaining}")
    if seconds > 0:
        time_countdown = window.after(1000, countdown, seconds - 1)
    else:    
        reps += 1
        if reps % 2 == 0:
            tick_index += 1
            label_2.config(text= "✅" * tick_index)
        window.after(1000, start_timer)
      
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, background= YELLOW)

canvas = Canvas(width= 200, height= 224, background= YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file= r"Pomodoro\Assets\tomato.png")
canvas.create_image(100, 112, image= tomato_image)
timer = canvas.create_text(100, 130, text= "00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row= 1, column= 1)

label_1 = Label(text="Timer", font= (FONT_NAME, 45, "bold"), background= YELLOW, foreground= ORANGE)
label_1.grid(row= 0, column= 1, pady= (0, 20))

label_2 = Label(text= "", font= (FONT_NAME, 20, "bold"), background= YELLOW, foreground= ORANGE)
label_2.grid(row= 3, column= 1, pady= (30, 0))

style = ttk.Style()
style.configure("C.TLabel", padding=[20,10,20,0], font= (FONT_NAME, 20, "bold"), background= YELLOW, foreground= ORANGE)
style.map("C.TLabel", background=[('disabled', YELLOW), ('active', ORANGE)], foreground=[('disabled', YELLOW), ('active', LIGHT_ORANGE)])

button_1 = ttk.Button(text= "Start", style= "C.TLabel", command= start_timer)
button_1.grid(row=2, column= 0, pady= (20, 0))

button_2 = ttk.Button(text= "Reset", style= "C.TLabel", command= reset_timer)
button_2.grid(row= 2, column= 2 , pady= (20, 0))

window.mainloop()