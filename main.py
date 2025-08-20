from tkinter import *
import tkinter as tk
import ttkbootstrap as tb
import secrets
import string

# Generate a random password based on selected options
def generate_password():
    characters = ""
    if use_uppercase.get():
        characters += string.ascii_uppercase
    if use_lowercase.get():
        characters += string.ascii_lowercase
    if use_numbers.get():
        characters += string.digits
    if use_special.get():
        characters += string.punctuation
    
    if not characters:
        password_var.set("Select at least one option!")
        return
    
    new_password = ''.join(secrets.choice(characters) for i in range(12))
    password_var.set(new_password)

# Copy text to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()

# Initialize window
root = tb.Window(themename="superhero")
root.title("Random Password Generator")
root.geometry('500x400')

# Title
title = Label(root, text="PSWD GEN", font=("Impact", 20))
title.pack(pady=10)

# Password field + Copy button (Side by side)
password_frame = Frame(root)
password_frame.pack(pady=20)

password_var = tk.StringVar(value="Click 'Generate New'")
password_field = tb.Entry(password_frame, textvariable=password_var, state='readonly', width=30)
password_field.pack(side=LEFT, padx=(0, 5))

copy_button = tb.Button(password_frame, text="Copy", command=copy_to_clipboard)
copy_button.pack(side=LEFT)

# Checkboxes for options
use_uppercase = tk.BooleanVar(value=True)
use_lowercase = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=True)

checkbox_frame = Frame(root)
checkbox_frame.pack(pady=10)

tb.Checkbutton(checkbox_frame, text="Include Uppercase", variable=use_uppercase).grid(row=0, column=0, sticky='w')
tb.Checkbutton(checkbox_frame, text="Include Lowercase", variable=use_lowercase).grid(row=1, column=0, sticky='w')
tb.Checkbutton(checkbox_frame, text="Include Numbers", variable=use_numbers).grid(row=2, column=0, sticky='w')
tb.Checkbutton(checkbox_frame, text="Include Special Characters", variable=use_special).grid(row=3, column=0, sticky='w')

# Buttons for Generate
generate_button = tb.Button(root, text="Generate New", command=generate_password)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
