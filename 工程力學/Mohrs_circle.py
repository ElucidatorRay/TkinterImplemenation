# Mohrs circle
import tkinter as tk
import math
import numpy as np
import matplotlib.pyplot as plt

window = tk.Tk()
window.title('Mohrs circle')
window.geometry('800x750')
Title = tk.Label(window,text = 'This is a calculator to generate the correspond\nMOHRS CIRCLE'
                 ,font = ('ARial',20),width = 50, height = 2,bg = 'white')
Title.place(x = 0,y = 0,anchor = 'nw')
i = 0
img = img = tk.PhotoImage(file = f'{i}-th.png')
def plot_circle(C_x,R):
    global i
    i += 1
    theta = np.arange(0,2*math.pi,0.001)
    theta = tuple(theta)
    circle_x = [C_x + R*math.cos(elem) for elem in theta]
    circle_y = [R*math.sin(elem) for elem in theta]
    plt.plot(circle_x,circle_y,label = f'{i}-th',linewidth = 1.0)
    
    plt.xlabel('sigma')
    plt.ylabel('tao')
    ax = plt.gca()
    ax.invert_yaxis()
    plt.legend(loc = 'best', fontsize = 9, title = f'{i}-th')
    plt.savefig(fname = f'{i}-th.png', format = "png")

def generate():
    global i
    global img
    var1 = float(E1.get())
    var2 = float(E2.get())
    var3 = float(E3.get())
    var4 = float(E4.get())
    R = math.pow(((var1 - var2)/2)**2 + var3**2,0.5)
    C_x = (var1 + var2)/2
    if C_x > 0:
        max1 = C_x + R
    else:
        max1 = abs(C_x - R)
    max2 = R
    plot_circle(C_x,R)
    img = tk.PhotoImage(file = f'{i}-th.png')
    img_now = canvas.create_image(300,160,anchor = 'center',image = img)
    lb1.insert('end',max1)
    lb2.insert('end',max2)

P1 = tk.Label(window,text = 'The Sigma-X is : ',font = ('ARial',15)).place(x = 70,y = 80)
P2 = tk.Label(window,text = 'The Sigma-Y is : ',font = ('ARial',15)).place(x = 420,y = 80)
P3 = tk.Label(window,text = 'The Tao-XY is : ',font = ('ARial',15)).place(x = 70,y = 120)
P4 = tk.Label(window,text = 'The theta is : ',font = ('ARial',15)).place(x = 420,y = 120)
A1 = tk.Label(window,text = 'The max sigma is :',font = ('ARial',15)).place(x = 100,y = 560)
A2 = tk.Label(window,text = 'The max tao is : ',font = ('ARial',15)).place(x = 480,y = 560)

E1 = tk.Entry(window)
E1.place(x = 260,y = 86)
E2 = tk.Entry(window)
E2.place(x = 610,y = 86)
E3 = tk.Entry(window)
E3.place(x = 260,y = 126)
E4 = tk.Entry(window)
E4.place(x = 610,y = 126)

lb1 = tk.Listbox(window,width = 20,height = 5,font = ('ARial',15))
lb1.place(x = 100,y = 590)
lb2 = tk.Listbox(window,width = 20,height = 5,font = ('ARial',15))
lb2.place(x = 480,y = 590)

canvas = tk.Canvas(window,bg = 'white',height = 300,width = 600)
Generate = tk.Button(window,text = 'Generate the circle',width = 30,height = 1
                    ,font = ('ARial',15),bg = 'yellow',command = generate).place(x = 400,y = 200,anchor = 'center')

img_now = canvas.create_image(300,160,anchor = 'center',image = img)
canvas.place(x = 400,y = 400,anchor = 'center')

window.mainloop()