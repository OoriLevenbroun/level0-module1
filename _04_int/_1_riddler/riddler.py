from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score = 0
    messagebox.showinfo(title='the riddler', message='answer me three riddles')
    heaven_and_earth = simpledialog.askstring(title='riddle number 1', prompt='What is one thing that all wise men, regardless of their politics or religion, agree is between heaven and earth?')
    if heaven_and_earth == 'and' or heaven_and_earth == 'the word and':
        score += 1
    starting = simpledialog.askstring(title='riddle number 2', prompt='What 8 letter word can have a letter taken away and it still makes a word. Take another letter away and it still makes a word. Keep on doing that until you have one letter left. What is the word?')
    if starting == 'starting':
        score += 1
    key = simpledialog.askstring(title='riddle numbe  3', prompt='What has many keys, but cant even open a single door?')
    if key == 'a paino' or key == 'paino':
        score += 1
    if score == 3:
        messagebox.showinfo(title='your score', message='you answered ' + str(score) + ' riddles correctly')
    else:
        messagebox.showerror(title='DuMb', message='you only answered ' + str(score) + ' riddles correctly, you idiot')
"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
