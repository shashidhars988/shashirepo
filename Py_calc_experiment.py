from tkinter import*

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
cal = Tk()
cal.title("Calculator")
operator=""
text_Input = StringVar()

txtDisplay = Entry(cal,font=('TimesNewRoman', 15), textvariable=text_Input,
                   bd = 10, insertwidth=4,
                   bg="gery", justify='right').grid(columnspan=4)

bt7 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
bt8 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
bt9 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
add = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="+",command=lambda:btnClick("+")).grid(row=1,column=3)
#=========================================================================

bt4 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
bt5 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
bt6 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
sub = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="-",command=lambda:btnClick("-")).grid(row=2,column=3)
#=========================================================================

bt1 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="1",command=lambda:btnClick(1)).grid(row=3,column=0)
bt2 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
bt3 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
mul = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="*",command=lambda:btnClick("*")).grid(row=3,column=3)
#=========================================================================

bt0 = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="0",command=lambda:btnClick(0)).grid(row=4,column=0)
clr = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="C",command=btnClear).grid(row=4,column=1)
eq = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="=",command=btnEqual).grid(row=4,column=2)
div = Button(cal,padx=16,bd=4, fg="black",font=('TimesNewRoman', 15),
             text="/",command=lambda:btnClick("/")).grid(row=4,column=3)
cal.mainloop()
