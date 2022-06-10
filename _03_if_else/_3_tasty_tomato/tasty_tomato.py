from tkinter import simpledialog
import tkinter as tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
color = simpledialog.askstring(title='a tomato collor', prompt='enter a tomato color, you can chose between yelllow red or green')

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if color == 'red':
 canvas.create_oval(75, 200, 400, 450, fill="red", outline="red")
if color == 'yellow':
 canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="yellow")
if color == 'green':
 canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="green")

root.mainloop()
