from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

def addToInput(character):
    e.insert(len(e.get()), str(character))

def clear():
    e.delete(0, END)

def EqualResult ():
    question = e.get()
    clear()
    eval('e.insert(0,{0})'.format(question))
    

button1 = Button(root, text='1', padx=40, pady=20, command=lambda: addToInput(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: addToInput(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: addToInput(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: addToInput(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: addToInput(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: addToInput(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: addToInput(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: addToInput(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: addToInput(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: addToInput(0))
button_add = Button(root, text='+', padx=39, pady=20, command=lambda: addToInput('+'))
button_track = Button(root, text='-', padx=39, pady=20, command=lambda: addToInput('-'))
button_multipy = Button(root, text='x', padx=39, pady=20, command=lambda: addToInput('*'))
button_divide = Button(root, text=':', padx=39, pady=20, command=lambda: addToInput('/'))
button_equal = Button(root, text='=', padx=91, pady=20, command=EqualResult)
button_clear = Button(root, text="clear", padx=79, pady=20, command=clear)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)
button_track.grid(row=5, column=0)
button_multipy.grid(row=5, column=1)
button_divide.grid(row=5, column=2)
root.mainloop()
