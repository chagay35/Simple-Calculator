from tkinter import * # import everything from tkinter module

expression = "" # global variable for the expression

def press(num):
	"""update expression in the text entry box"""
	global expression
	expression = expression + str(num) # add string to the variable
	equation.set(expression) # update the expression by using set method

def equalpress():
	"""evaluate the final expression"""
	try:  # Try and except statement is used for handling the errors like divide by 0 error etc. Put that code inside the try block which may generate the error
		global expression
		total = str(eval(expression)) # eval func evaluate the expression and then str to convert the result into string
		equation.set(total)
		expression = "" # initialize the expression variable by empty string
	except: # if error happened then handle by the except block
		equation.set(" error ")
		expression = ""

def clear():
	"""clear the text entry box"""
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__": # Driver code
	gui = Tk() # create a GUI window
	gui.configure(background="white") # set the background color for the window
	gui.title("Calculator")
	#gui.geometry("265x125")
	equation = StringVar() #this is the variable class to create an instance of this class
	expression_field = Entry(gui, textvariable=equation) #create the text entry box
	expression_field.grid(columnspan=4, ipadx=70) # grid method is used for placing the widgets at respective position
	equation.set('enter your expression')
	# now we create Buttons and place them at a particular location inside the root window . when button is pressed, the command or function affiliated to that button is executed .
	button1 = Button(gui, text=' 1 ', fg='black', bg='grey',command=lambda: press(1), height=3, width=8)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='grey',command=lambda: press(2), height=3, width=8)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='grey',command=lambda: press(3), height=3, width=8)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='grey',command=lambda: press(4), height=3, width=8)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='grey',command=lambda: press(5), height=3, width=8)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='grey',command=lambda: press(6), height=3, width=8)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='grey',command=lambda: press(7), height=3, width=8)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='grey',command=lambda: press(8), height=3, width=8)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='grey',command=lambda: press(9), height=3, width=8)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='grey',command=lambda: press(0), height=3, width=8)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='grey',command=lambda: press("+"), height=3, width=8)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='grey',command=lambda: press("-"), height=3, width=8)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='grey',command=lambda: press("*"), height=3, width=8)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='grey',command=lambda: press("/"), height=3, width=8)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='grey',command=equalpress, height=3, width=8)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='grey',command=clear, height=3, width=8)
	clear.grid(row=5, column=1)

	gui.mainloop() # start the GUI