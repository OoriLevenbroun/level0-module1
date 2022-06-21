from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    messagebox.showerror(title='warning!')
    for i in range(2):
        for i in range(12):
            messagebox.showinfo( message='badger, ')
        for i in range(2):
            messagebox.showinfo(message='mushroom, ')
    messagebox.showinfo(message='a snake!')
