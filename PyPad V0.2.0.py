from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys

root = Tk()
root.title("Py-Pad")
root.geometry("930x645")
root.iconbitmap("py-pad3.ico")

current_file_path = None

####file options def####
def new_file():
    global current_file_path
    current_text = text_area.get("1.0", END).strip()

    if current_text:  # If there's any text
        response = messagebox.askyesnocancel("Save Changes?", "Do you want to save changes before starting a new file?")
        
        if response:  # Yes
            save_file()
        elif response is None:  # Cancel
            return  # Don't continue

    # Clear text area and reset file path
    text_area.delete("1.0", END)
    current_file_path = None
    root.title("Py-Pad")
    update_status()  # Update status bar

def open_file():
    global current_file_path
    path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        initialfile="untitled.txt"
    )
    if path:
        current_file_path = path
        with open(path, 'r') as file:
            content = file.read()
            text_area.delete("1.0", END)
            text_area.insert(END, content)
            update_status()  # Update status bar

def save_file():
    global current_file_path
    if current_file_path:
        with open(current_file_path, 'w') as file:
            file.write(text_area.get("1.0", END))
       
def save_as_file():
    global current_file_path
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        initialfile="untitled.txt"
    )
    if path:
        current_file_path = path
        with open(path, 'w') as file:
            file.write(text_area.get("1.0", END))

def update_status():
    """Update the status bar with word and line counts"""
    text = text_area.get("1.0", END)
    words = len(text.split())
    lines = len(text.splitlines())
    status_label.config(text=f"Words: {words} | Lines: {lines}")

def on_text_change(event=None):
    """Called when text changes to update status"""
    update_status()

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
text_area.pack(expand=True, fill='both', padx=0, pady=0)

# Create status bar at the bottom
status_bar = Frame(root, relief=SUNKEN, bd=1)
status_bar.pack(side=BOTTOM, fill=X)

status_label = Label(status_bar, text="Words: 0 | Lines: 0", anchor=W)
status_label.pack(side=LEFT, padx=5, pady=2)

# Bind text change events to update status
text_area.bind('<KeyRelease>', on_text_change)
text_area.bind('<Button-1>', on_text_change)

# Initial status update
update_status()

root.mainloop()