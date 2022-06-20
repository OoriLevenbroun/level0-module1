from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    add = simpledialog.askinteger(title='enter a numbers', prompt='enter one numbers you want to add')
    add2 = simpledialog.askinteger(title='enter another numper', prompt='enter the secound number you want to add to ' + str(add))
    messagebox.showinfo(title='this is your answer',message=add+add2)
"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
