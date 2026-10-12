import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from rembg import remove
import sqlite3
import json
import os

root = tk.Tk()
root.title("Image Background Remover")
root.geometry("800x600")
root['bg'] = "#e0aec0"


canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

frame = tk.Frame(root, bg="#e0aec0")
frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(frame, text="Image Background Remover", font=("Helvetica", 24), bg="#9d4263")
input_label = tk.Label(frame, text="Input Image:", font=("Helvetica", 16), bg="#e0aec0")
button = tk.Button(frame, text="Remove Background", font=("Helvetica", 16), command=lambda: messagebox.showinfo("Info", "Background removed!"))
title_label.pack(pady=20)
input_label.pack(pady=10)
button.pack(pady=20)


input_img = Image.open('input.jpg')
output_img = remove(input_img)
output_img.save('output.png')


root.mainloop()
