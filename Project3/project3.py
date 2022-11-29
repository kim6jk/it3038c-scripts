import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import csv

# this is a function to get the selected radio button value
def getRadioButtonValue():
	buttonSelected = rbType.get()
	return buttonSelected
# funciton to disable/enable the OptionMenu when plot is selected 
def changeState():
    if (getRadioButtonValue() == 1):
        drop.configure(state="normal")
    else:
        drop.configure(state="disabled")
# function to handle selecting a file, then parsing the file and ordering the plot points ascending and add it to and x & y array
def selectFile():
    global filename
    filename = askopenfilename()
    global x, y
    x=[]
    y=[]
    # Open the selected file in 'r' (Read) mode from https://www.pythonprogramming.net/loading-file-data-matplotlib-tutorial/
    with open(filename,'r') as file:
        points = csv.reader(file, delimiter = ',')
        # This sorts the list of points by the X value // learned about lambda sorting here https://pythonsolved.com/how-to-sort-2d-array-in-python/
        points = sorted(points, key = lambda i: int(i[0]))
        for value in points:
            x.append(int(value[0]))
            y.append(int(value[1]))
# function to change a global variable to get line style from the OptionMenu to the graphIt function
def setStyle(lineStyle):
    global ls
    ls = lineStyle
# function with checks to create the correct graph based on user choices and then plot it
def graphIt():
    graph = getRadioButtonValue()
    if(graph == 1):
        if(ls == "Solid"):
            plt.plot(x,y,'-')
        elif(ls == "Dot"):
            plt.plot(x,y,':')
        elif(ls == "Dash"):
           	plt.plot(x,y,'--')
        elif(ls == "Dash & Dot"):
            plt.plot(x,y,'-.')
    elif(graph == 2):
        plt.scatter(x,y)
    elif(graph == 3):
        plt.bar(x,y)
    elif(graph == 4):
        plt.step(x,y)
    plt.show()

# create the root window
root = Tk()

rbType = tk.IntVar()
rbLine = tk.StringVar()
ls = "Solid"

# set the size of the gui and set the background color and title
root.geometry('300x300')
root.configure(background='#FAEBD7')
root.title('Project 3')

# Create a set of radio buttons for graph type selection
frame=Frame(root, width=0, height=0, bg='#FAEBD7')
frame.place(x=37, y=28)
ARBEES=[
('Plot', '1'),
('Scatter', '2'),
('Bar', '3'),
('Step', '4'),
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(frame, text=text, variable=rbType, value=mode, bg='#FAEBD7', font=('arial', 12, 'normal'),command=changeState)
	rbGroupOne.pack(side='top', anchor = 'w')
# Create OptionMenu for graph style selection
frame=Frame(root, width=0, height=0, bg='#FAEBD7')
frame.place(x=120, y=28)
lineStyles = [
	"Solid",
	"Dot",
	"Dash",
	"Dash & Dot"
]
rbLine.set("Solid")
drop = OptionMenu(frame, rbLine, *lineStyles, command=setStyle)
drop.configure(state="disabled")
drop.pack()
# create a button to call the selectFile function
frame=Frame(root, width=0, height=0, bg='#FAEBD7')
frame.place(x=120,y=75)
filePicker = Button(frame, text="Select a File", command=selectFile)
filePicker.pack()
# create a button to call the graphIt function
frame=Frame(root, width=0, height=0, bg='#FAEBD7')
frame.place(x=50,y=175)
graph = Button(frame, text="Graph it!", command=graphIt)
graph.pack()

root.mainloop()
