from tkinter import*
"""
Author: Raymond Bernard GADJI
Name: Ivorian calculator
For: This is a calculator programming software
Year: 2021
Version: 1
(c) 2021 - Yedidia Industries
"""

# display whatever the user clicks on
def btnOnClick(numb):
    global operator  # operator will hold my expressions for manipulation
    operator = operator + str(numb);
    text_input.set(operator);
    

# perfom the user's operation and display the result 
def btnEqual():
    try:
        global operator
        Op_res = str(eval(operator));
        text_input.set(Op_res);
        operator = "";
    # if error is generate then handle
    except:
        text_input.set("Invalid Operation")
#         messagebox.showerror("An error has occurred", "Invalid Operation")
        operator = "";

# clearing everything on sreen
def btnClear():
    global operator
    operator = "";
    text_input.set("");
   
UiCal = Tk();
UiCal.title("Ivorian Calculator")
# UiCal.geometry("200x300") # set GUI size in pixel: width x height
operator = ""
text_input = StringVar()

# display screen creation (i.e. an entry text)
txtDisplay = Entry(UiCal,
           font = ('Comic Sans MS', 20, 'bold'),
           textvariable = text_input,
           bd = 5,
           insertwidth = 4,
           fg = 'blue',
           bg = 'white',
           justify = 'right').grid(columnspan=4);

# creation of buttons - From 0 to 7
btn1 = Button(UiCal,
             padx = 20, 
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '0',
             command = lambda:btnOnClick(0),
             height=1, width=2).grid(row=4, column=0)

btn2 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '1',
             command = lambda:btnOnClick(1),
             height=1, width=2).grid(row=3, column=0)

btn3 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '4',
             command = lambda:btnOnClick(4),
             height=1, width=2).grid(row=2, column=0)

btn4 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '7',
             command = lambda:btnOnClick(7),
             height=1, width=2).grid(row=1, column=0)

# creation of buttons - 2 - 5 - 8

btn5 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '',
             height=1, width=2).grid(row=4, column=1)
             

btn6 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '2',
             command = lambda:btnOnClick(2),
             height=1, width=2).grid(row=3, column=1)

btn7 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '5',
             command = lambda:btnOnClick(5),
             height=1, width=2).grid(row=2, column=1)

btn8 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '8',
             command = lambda:btnOnClick(8),
             height=1, width=2).grid(row=1, column=1)

# creation of buttons from 3 to 9

btn9 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '',
             height=1, width=2).grid(row=4, column=2)

btn10 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '3',
             command = lambda:btnOnClick(3),
             height=1, width=2).grid(row=3, column=2)

btn11 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '6',
             command = lambda:btnOnClick(6),
             height=1, width=2).grid(row=2, column=2)

btn12 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '9',
             command = lambda:btnOnClick(9),
             height=1, width=2).grid(row=1, column=2)

# creation of buttons - From plus to division

btn13 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '+',
             command = lambda:btnOnClick("+"),
             height=1, width=2).grid(row=4, column=3)

btn14 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '-',
             command = lambda:btnOnClick("-"),
             height=1, width=2).grid(row=3, column=3)

btn15 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '*',
             command = lambda:btnOnClick("*"),
             height=1, width=2).grid(row=2, column=3)


# creation of buttons - From Quit to Equal


div_btn3 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '/', # or '÷' equally as valid
             command = lambda:btnOnClick("/"), # or '÷' equally as valid
             height=1, width=2).grid(row=1, column=3)

Eqbtn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '=',
             command = btnEqual,
             height=1, width=2).grid(row=1, column=4)

Clrbtn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = 'Clear',
             command = btnClear,
             height=1, width=2).grid(row=3, column=4)

Quitbtn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = 'Quit',
             command = UiCal.destroy, # Which will close the GUI
             height=1, width=2).grid(row=4, column=4)


# creation of button SQROOT button

import math
def sqrt(number):
   if "number" == int():
      number = eval(input("Enter your number "));
   elif "number" == int():
      print("press on √")
      sq_number = math.sqrt(number)
      print("The square root of ", number, "is", sq_number)
      operator = "";
#    else:
#       print("Enter your number ")
#       operator = "";
         
btn16 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '√',
             command = sqrt('number'),
             height=1, width=2).grid(row=2, column=4)


                     
# start the App
UiCal.mainloop()