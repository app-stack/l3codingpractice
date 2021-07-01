from tkinter import*
"""
Author: F.J

Some terms to define:
padding = the space between its content and its border.
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
UiCal.title("Demo Calculator")
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

# creation of buttons
btn1 = Button(UiCal,
             padx = 20, # you can also add pady = 16
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '0',
             command = lambda:btnOnClick(0),
             height=1, width=2).grid(row=1, column=0)

btn2 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '1',
             command = lambda:btnOnClick(1),
             height=1, width=2).grid(row=1, column=1)

div_btn3 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '/', # or '÷' equally as valid
             command = lambda:btnOnClick("/"), # or '÷' equally as valid
             height=1, width=2).grid(row=1, column=2)

Eqbtn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '=',
             command = btnEqual,
             height=1, width=2).grid(row=1, column=3)

Clrbtn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = 'Cl',
             command = btnClear,
             height=1, width=2).grid(row=2, column=0)

Quitbtn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = 'Quit',
             command = UiCal.destroy, # use destroy to close GUI
             height=1, width=2).grid(row=2, column=3)
                     
# start the App
UiCal.mainloop()