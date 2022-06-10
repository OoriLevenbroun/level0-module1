from tkinter import simpledialog, messagebox ,Tk
if __name__ == '__main__':
    window = Tk()
    rem = simpledialog.askstring(title='who is remarkable', prompt='enter a name to find out somehting remarkable about them')
    if rem == 'zach' or rem == 'Zach':
        messagebox.showinfo(title='tH1s p3R50N I5 R3MarKaBl3', message='zach is remakable becuase he is cool')
    if rem == 'edric' or rem == 'Edric':
        messagebox.showinfo(title='tH1s p3R50N I5 R3MarKaBl3', message='edric is remarkable becuase he can code')
    if rem == 'beck' or rem == 'Beck':
        messagebox.showinfo(title='tH1s p3R50N I5 R3MarKaBl3', message='beck is remarkable becuase he is smart')
    if rem == 'aaron' or rem == 'Aaron':
        messagebox.showinfo(title='tH1s p3R50N I5 R3MarKaBl3', message='aaron is remakable becuase he dosent know')
    if rem == 'sebastian' or rem == 'Sebastian':
        messagebox.showinfo(title='tH1s p3R50N I5 R3MarKaBl3', message='sebastian is remakable becuase he dosent know')
    else:
        messagebox.showerror(title='???????', message='this person does not exist')
