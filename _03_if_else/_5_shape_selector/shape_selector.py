import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    a = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='enter a shape', prompt='enter a shape')
    if shape == 'square':
        for i in range(4):
            a.forward(100)
            a.right(90)
    elif shape == 'triangle' or shape == 'tri':
        for i in range(3):
            a.forward(100)
            a.right(360/3)
    elif shape == 'pentagon' or shape == 'pen':
        for i in range(5):
            a.forward(100)
            a.left(360/5)
    elif shape == 'hexagon' or shape == 'hex':
        for i in range(6):
            a.forward(100)
            a.right(360/6)
    elif shape == 'heptagon' or shape == 'hep':
        for i in range(7):
            a.forward(100)
            a.right(360/7)
    elif shape == 'octagon' or shape == 'octa':
        for i in range(8):
            a.forward(100)
            a.right(360/8)
    else:
        messagebox.showerror(title='error', message='ethier this shape does not exist or it is to complex for mere mortals to comprehand')
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
    a.done()
