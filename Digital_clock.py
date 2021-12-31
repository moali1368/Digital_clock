# Import Time and tkinter Library
from time import strftime 
from tkinter import *

# import time function 
def time():
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000, time)

# Import Tk class as tkinter Library to make Frame
window = Tk() 

# Create Frame Tittle "clock"
window.title("clock") 

# Create varible label to make Label function 
label = Label(window, font= ("ds-digital", 80), background="black", foreground="cyan") 
label.pack(anchor="center")

time()

# import mainloop function to avoid clossing The Frame
mainloop() 
