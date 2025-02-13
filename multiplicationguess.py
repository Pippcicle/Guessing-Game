from tkinter import *
#from tkinter.ttk import *
import tkinter.messagebox
import random

root=Tk()
root.minsize(400,400)
root.title("Guess the Multiplication")

heading = Label(root, text = "Guess the Multiplication", background = '#FF9FB2', foreground = '#FBDCE2', font = ('comic sans', 18, 'bold'))
heading.pack()
name = Label(root, text = "Enter Your Name : ", foreground = '#50858B', font = ('comic sans', 12, 'bold'))
name.place(x=10, y=50)
name_input = Entry(root, width = 25)
name_input.place(x=10, y = 90)
ok_btn = Button(root, text = 'ok', font = ('comic sans', 12, 'bold'), background = '#50858B', foreground = '#78CAD2', width = 10)
ok_btn.place(x = 200, y = 70)

guess_lbl = Label(root, text = " Enter your Guess : ", font = ('comic sans', 12, 'bold'), foreground= '#6665DD')
guess_lbl.place( x = 10, y = 200)
guess_input = Entry(root, width = 25)
guess_input.place(x= 10, y = 240)
guess_btn = Button(root, text = "Guess", font = ('comic sans', 12, 'bold'), background= '#6665DD', foreground= '#9B9ECE', width = 10)
guess_btn.place(x = 200, y = 220)

root.mainloop()