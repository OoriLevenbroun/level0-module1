from tkinter import messagebox, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    for i in range(1000):
        messagebox.showinfo(title='BANANA!', message='BANANA!')
    messagebox.showinfo(title='orange', message='orange you glad it didnt say banana?')
    messagebox.showinfo(title='wow', message='wow, you survived, give yourself a pat on the back')
"""
 * Write a python program that prints the word 'banana' one thousand (1,000) times
"""

