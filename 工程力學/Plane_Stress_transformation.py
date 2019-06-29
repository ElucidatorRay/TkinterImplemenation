# Plane-Stress transformation
import tkinter as tk
import math

window = tk.Tk()
window.title('Plane-Stress transformation')
window.geometry('800x750')

ans_x = tk.DoubleVar()
ans_y = tk.DoubleVar()
ans_xy = tk.DoubleVar()
ans_theta_max = tk.DoubleVar()
ans_x.set(0)
ans_y.set(0)
ans_xy.set(0)
ans_theta_max.set(0)

def calculate():
    var1 = E1.get()
    var2 = E2.get()
    var3 = E3.get()
    var4 = E4.get()
    
    var1 = float(var1)
    var2 = float(var2)
    var3 = float(var3)
    var4 = float(var4)
    
    ans1 = get_new_sigma_x(var1,var2,var3,var4)
    ans2 = get_new_sigma_y(var1,var2,var3,var4)
    ans3 = get_new_tao_xy(var1,var2,var3,var4)
    ans_x.set(ans1)
    ans_y.set(ans2)
    ans_xy.set(ans3)
    if var1 - var2 != 0:
        ans_theta_max.set(math.atan(2*var3/(var1 - var2))/math.pi/2*360/2)
    else:
        ans_theta_max.set(9999999999999999999)
def get_new_sigma_x(x,y,tao,theta):
    theta = float(theta)/360*2*math.pi
    return (x + y)/2 + (x - y)/2*math.cos(2*theta) + tao*math.sin(2*theta)
def get_new_sigma_y(x,y,tao,theta):
    theta = float(theta)/360*2*math.pi
    return (x + y)/2 - (x - y)/2*math.cos(2*theta) - tao*math.sin(2*theta)
def get_new_tao_xy(x,y,tao,theta):
    theta = float(theta)/360*2*math.pi
    return (-1)*(x - y)/2*math.sin(2*theta) + tao*math.cos(2*theta)

Title = tk.Label(window,text = 'This is a calculator of\nGENERAL EQUATION OF PLANE-STRESS TRANSFORMATION'
                 ,font = ('ARial',20),width = 50, height = 2,bg = 'white')
Title.place(x = 0,y = 0,anchor = 'nw')
Prompt = tk.Label(window,text = 'consider the original plane and stress is below'
                  ,font = ('ARial',15),width = 50, height = 1,bg = 'light blue')
Prompt.place(x = 120,y = 70)

canvas = tk.Canvas(window,bg = 'white',height = 300,width = 300)
img1 = tk.PhotoImage(file = '123.gif')
img_ori = canvas.create_image(160,150,anchor = 'center',image = img1)
canvas.place(x = 200,y = 260,anchor = 'center')

P1 = tk.Label(window,text = 'The Sigma-X is : ',font = ('ARial',15)).place(x = 370,y = 130)
P2 = tk.Label(window,text = 'The Sigma-Y is : ',font = ('ARial',15)).place(x = 370,y = 200)
P3 = tk.Label(window,text = 'The Tao-XY is : ',font = ('ARial',15)).place(x = 370,y = 270)
P4 = tk.Label(window,text = 'The theta is : ',font = ('ARial',15)).place(x = 370,y = 340)

E1 = tk.Entry(window)
E1.place(x = 550,y = 135)
E2 = tk.Entry(window)
E2.place(x = 550,y = 205)
E3 = tk.Entry(window)
E3.place(x = 550,y = 280)
E4 = tk.Entry(window)
E4.place(x = 550,y = 350)

A1 = tk.Label(window,text = 'The new sigma-X is :',font = ('ARial',15)).place(x = 100,y = 450)
A2 = tk.Label(window,text = 'The new sigma-Y is :',font = ('ARial',15)).place(x = 100,y = 520)
A3 = tk.Label(window,text = 'The new Tao-XY is :',font = ('ARial',15)).place(x = 100,y = 590)
A4 = tk.Label(window,text = 'The theta-p is :',font = ('ARial',15)).place(x = 100,y = 660)

text1 = tk.Label(window,width = 30,height = 1,font = ('ARial',15),textvariable = ans_x)
text1.place(x = 300,y = 454)
text2 = tk.Label(window,width = 30,height = 1,font = ('ARial',15),textvariable = ans_y)
text2.place(x = 300,y = 524)
text3 = tk.Label(window,width = 30,height = 1,font = ('ARial',15),textvariable = ans_xy)
text3.place(x = 300,y = 594)
text4 = tk.Label(window,width = 30,height = 1,font = ('ARial',15),textvariable = ans_theta_max)
text4.place(x = 300,y = 664)

Calculate = tk.Button(window,text = 'Calculate',width = 30,height = 1
                      ,font = ('ARial',15),bg = 'yellow',command = calculate).place(x = 370,y = 390)

window.mainloop()