from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num = simpledialog.askinteger(title='enter a number', prompt='enter a number')
    num2 = simpledialog.askinteger(title='enter a 2nd number', prompt='enter another number')
    op = simpledialog.askstring(title='what operaatoin to use', prompt='do you want to +(add), -(subtract), /(devide) or *(multiply)')
    add = num+num2
    sub = num-num2
    dev = num/num2
    mul = num*num2
    if op == '+' or op == 'add':
        messagebox.showinfo(title='your answer:', message=num + ' + ' + num2 + ' = ' + )
"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
