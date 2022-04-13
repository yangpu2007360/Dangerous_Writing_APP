import tkinter
from tkinter import *
import time
from tkinter import messagebox
import sys
import os
import schedule
import sched
from threading import Timer

root = Tk()
root.geometry("800x700")
warning_text = "Warning: this is a dangerous writing app. \nIf you stop typing for 5 seconds, \nall the words you entered will be removed."

number_of_words = 0
count = 0
repeat_check = False

def start_timer():

    print("start counting time")
    startButton["state"] = "disabled"
    inputtxt.focus_set()
    check_speed()


def check_speed():
    global count, number_of_words, repeat_check
    rounded_time = 5
    text_entered = inputtxt.get("1.0", END)
    current_number = len(text_entered.split())
    print(current_number)
    number_dif = current_number - number_of_words
    print(count)


    if count != 0 and number_dif < 1:
        message = f"Your typing speed is too low!"
        tkinter.messagebox.showinfo(title="Too slow!", message=message)
        restart_program()

    root.after(5000, check_speed)
    count = count + 1
    number_of_words = current_number


myLabel = Label(root, text="Dangerous Writing App", font=("Arial", 24, "bold"), pady=15)

testingLabel = Label(root, pady=10, fg='red',
                     text=warning_text,
                     font=("Arial", 18,))


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


def save_text():
    global count, repeat_check
    text_entered = inputtxt.get("1.0", END)
    with open('masterpiece.txt', 'w') as f:
        f.write(text_entered)
    message = f"Text has been saved. keep going!"
    tkinter.messagebox.showinfo(title="Saved!", message=message)
    startButton["state"] = "normal"
    count = 0



startButton = Button(root, text="Click when you are ready to start", command=start_timer)
saveButton = Button(root, text="Save the text", command=save_text)

inputtxt = Text(root, height=100, width=300, bg="light yellow")

myLabel.pack()
testingLabel.pack()
startButton.pack()
saveButton.pack()

inputtxt.pack()

root.mainloop()
