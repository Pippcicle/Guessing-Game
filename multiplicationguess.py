from tkinter import *
#from tkinter.ttk import *
import tkinter.messagebox
import random

root=Tk()
root.minsize(400,400)
root.title("Guess the Multiplication")

num1  = random.randint(1,10)
num2  = random.randint(1,10)
number = num1*num2
str_num1 = str(num1)
str_num2 = str(num2)

def namebutton():
    name = name_input.get()
    tkinter.messagebox.showinfo('HINT', 'Hello '+ name + ' What is ' + str_num1 + ' x ' + str_num2 + ' ? ')

def guess_num():
    guess = guess_input.get()
    guess = int(guess)
    
    if guess < number : 
        tkinter.messagebox.showinfo('TOO LOW', 'The guess is too low...')
    elif guess > number : 
        tkinter.messagebox.showinfo('TOO HIGH', 'The guess is too high...')
    else :
        tkinter.messagebox.showinfo('CORRECTT', 'WELL DONE')

heading = Label(root, text = "Guess the Multiplication", background = '#FF9FB2', foreground = '#FBDCE2', font = ('comic sans', 18, 'bold'))
heading.pack()
name = Label(root, text = "Enter Your Name : ", foreground = '#50858B', font = ('comic sans', 12, 'bold'))
name.place(x=10, y=50)
name_input = Entry(root, width = 25)
name_input.place(x=10, y = 90)
ok_btn = Button(root, text = 'ok', font = ('comic sans', 12, 'bold'), background = '#50858B', foreground = '#78CAD2', width = 10, command = namebutton)
ok_btn.place(x = 200, y = 70)

guess_lbl = Label(root, text = " Enter your Guess : ", font = ('comic sans', 12, 'bold'), foreground= '#6665DD')
guess_lbl.place( x = 10, y = 200)
guess_input = Entry(root, width = 25)
guess_input.place(x= 10, y = 240)
guess_btn = Button(root, text = "Guess", font = ('comic sans', 12, 'bold'), background= '#6665DD', foreground= '#9B9ECE', width = 10, command  = guess_num)
guess_btn.place(x = 200, y = 220)

root.mainloop()