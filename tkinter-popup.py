import tkinter as tk
from tkinter import Tk, Button

def mainw():  # Main Window
    window = Tk()
    window.geometry("400x150")
    window.title("Title ")
    button_name = Button(window,
                         text="Click Me",
                         command=command_name)  # Button commnad line 22
    button_name.pack(side=tk.TOP)
    Exit_Button = Button(window,
                         text="Exit",
                         fg="black",
                         command=quit)
    Exit_Button.pack(side=tk.BOTTOM)
    window.mainloop()

def command_name():  # command for button on line 13
    popup = Tk()
    NS = ""
    A = ""
    popup.title("Title  ")
    popup.geometry("450x150+10+20")
    Close_Button = Button(popup,
                          text="Close",
                          command=popup.destroy)
    Close_Button.pack(side=tk.BOTTOM)

mainw()
