from tkinter import *
import tkinter.messagebox

root = Tk()


root.title('Tic-Tac-Toe')

root.resizable(True,True)

click = True

count = 0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

xPhoto = PhotoImage(file = 'X.png')
oPhoto = PhotoImage(file = 'O.png')