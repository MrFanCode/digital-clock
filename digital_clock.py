from tkinter import *
import time


window = Tk()
window.title("Time")

def get_time():
    timeVar = time.strftime("%I:%M:%S:%p")
    clock.config(text=timeVar)
    clock.after(200, get_time)

clock = Label(window, font=("Calibri",90), foreground="green",background="black")
clock.pack()

get_time()
	
window.mainloop()
