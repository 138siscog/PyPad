from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import sys

root = Tk()
root.title("Py-Pad")
root.geometry("930x645")
####file options def####
def new_file():
    print("New File")

def open_file():
    print("Open File")

def save_file():
    print("Save File")

def save_as_file():
    print("Save As")

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
edit_menu = Menu(menubar, tearoff=0)
view_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="View", menu=view_menu)

file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save File", command=save_file) 
file_menu.add_command(label="Save As", command=save_as_file)

text_area = Text(root, wrap="word", width=80, height=20, font=("consolas", 11), padx=20, pady=20)
text_area.pack(expand=True, fill='both', padx=10, pady=10)

root.mainloop()