from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    age = simpledialog.askinteger(title='how old are you', prompt='enter your age')
    for i in range(age+1):
        messagebox.showinfo(title='your age was:', message=i)
