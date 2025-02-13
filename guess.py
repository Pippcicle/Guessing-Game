from tkinter import *
#from tkinter.ttk import *
import tkinter.messagebox
import random

root=Tk()
root.minsize(400,400)
root.title("Guess the number")

number  = random.randint(1,20)

def namebutton():
    name = name_input.get()
    tkinter.messagebox.showinfo('HINT', 'Hello '+ name + ' I am thinking of a number between 1 and 20')

def guess_num():
    guess = guess_input.get()
    guess = int(guess)
    
    if guess < number : 
        tkinter.messagebox.showinfo('LOW', 'The guess is too low...')
    elif guess > number : 
        tkinter.messagebox.showinfo('HIGH', 'The guess is too high...')
    else :
        tkinter.messagebox.showinfo('GOOD', 'WELL DONE')

heading = Label(root, text = "Guess the number", background = 'purple', foreground = 'pink', font = ('comic sans', 18, 'bold'))
heading.pack()
name = Label(root, text = "Enter Your Name : ", foreground = 'blue', font = ('comic sans', 12, 'bold'))
name.place(x=10, y=50)
name_input = Entry(root, width = 25)
name_input.place(x=10, y = 90)
ok_btn = Button(root, text = 'ok', font = ('comic sans', 12, 'bold'), background = '#BACDB0', foreground = '#2B3D41', width = 10, command = namebutton)
ok_btn.place(x = 200, y = 70)

guess_lbl = Label(root, text = " Enter your Guess : ", font = ('comic sans', 12, 'bold'), foreground= '#0077B6')
guess_lbl.place( x = 10, y = 200)
guess_input = Entry(root, width = 25)
guess_input.place(x= 10, y = 240)
guess_btn = Button(root, text = "Guess", font = ('comic sans', 12, 'bold'), background= '#90E0EF', foreground= '#03045E', width = 10, command  = guess_num)
guess_btn.place(x = 200, y = 220)

root.mainloop()
