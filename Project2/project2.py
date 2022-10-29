from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import csv

x = []
y = []

# Change the title of the matplotlib window
plt.title('Project 2!')

print('Use the file picker to load a .txt file with x,y value pair. Like the file provided on Github')
# I learned about this method from https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog
filename = askopenfilename()

print('What graph would you like?\n1) Plot\n2) Scatter\n3) Bar\n4) Step')
graph = int(input())

if (graph == 1):
        print('Which linestyle would you like?\n1) Solid\n2) Dotted\n3) Dashed\n4) Dash & Dot Alternating')
        ls = int(input())


# Open the selected file in 'r' (Read) mode from https://www.pythonprogramming.net/loading-file-data-matplotlib-tutorial/
with open(filename,'r') as file:
        points = csv.reader(file, delimiter = ',')
        # This sorts the list of points by the X value // learned about lambda sorting here https://pythonsolved.com/how-to-sort-2d-array-in-python/
        points = sorted(points, key = lambda i: int(i[0]))
        for value in points:
            x.append(int(value[0]))
            y.append(int(value[1]))

# Learned about matplotlib from their website specifically https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png
if(graph == 1):
        if(ls == 1):
                plt.plot(x,y,'-')
        elif(ls == 2):
                plt.plot(x,y,':')
        elif(ls == 3):
                plt.plot(x,y,'--')
        elif(ls == 4):
                plt.plot(x,y,'-.')
elif(graph == 2):
        plt.scatter(x,y)
elif(graph == 3):
        plt.bar(x,y)
elif(graph == 4):
        plt.step(x,y)

plt.show()
