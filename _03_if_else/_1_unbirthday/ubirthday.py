from tkinter import simpledialog, messagebox ,Tk
if __name__ == '__main__':
    window = Tk()
    bir = simpledialog.askstring(title='what is your birthday?', prompt='enter you birthday')
    if bir == '6/10':
        messagebox.showerror(title='happy birthday', message='HAPPY BIRTHDAY!!!')
    else:
        messagebox.showinfo(title='happy unbirthday', message='HAPPY UNBIRTHDAY!!!')
