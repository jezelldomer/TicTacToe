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

def play():
    button1 = Button(root,height=9,width=10,bd=.5,relief = 'ridge',bg = '#f2e6ff',textvariable = btn1,
                     command=lambda: press(1,0,0)) 
    button1.grid(row=0,column=0)

    button2 = Button(root,height=9,width=10,bd = .5,relief = 'ridge',bg = '#f2e6ff',textvariable = btn2,
                     command=lambda: press(2,0,1))
    button2.grid(row=0,column=1)

    button3 = Button(root,height=9,width=10,bd = .5,relief = 'ridge',bg = '#f2e6ff',textvariable = btn3,
                     command=lambda: press(3,0,2))
    button3.grid(row=0,column=2)

    button4 = Button(root,height=9,width=10,bd = .5,relief = 'ridge',bg = '#d9b3ff',textvariable = btn4,
                     command=lambda: press(4,1,0))
    button4.grid(row=1,column=0)

    button5 = Button(root,height=9,width=10,bd = .5,relief = 'ridge',bg = '#d9b3ff',textvariable = btn5,
                     command=lambda: press(5,1,1))
    button5.grid(row=1,column=1)

    button6 = Button(root,height=9,width=10,bd = .5,relief = 'ridge',bg = '#d9b3ff',textvariable = btn6,
                     command=lambda: press(6,1,2))
    button6.grid(row=1,column=2)

    button7 = Button(root,height=9,width=10,bd = .5,relief = 'ridge',bg = '#bf80ff',textvariable = btn7,
                     command=lambda: press(7,2,0))
    button7.grid(row=2,column=0)

    button8 = Button(root,height=9,width=10,bd = .5,relief = 'ridge',bg = '#bf80ff',textvariable = btn8,
                     command=lambda: press(8,2,1))
    button8.grid(row=2,column=1)

    button9 = Button(root,height=9,width=10,bd = .5,relief = 'ridge',bg = '#bf80ff',textvariable = btn9,
                     command=lambda: press(9,2,2))
    button9.grid(row=2,column=2)

