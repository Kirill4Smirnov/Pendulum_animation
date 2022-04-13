from tkinter import *
import time
from math import *

window_width = 1000
window_height = 600
theta0 = 1.0 #initial angle
theta_inc0 = 10.0 #initial angle speed
length = 1.0
g = 10.0
step = 0.01
fric = 0.5

y0 = 250

def create_window(window_width_, window_height_):
    window = Tk()
    window.title('Pendulum')
    window.geometry(f'{window_width_}x{window_height_}')
    return window

def create_canvas(window_, width_, height_):
    can = Canvas(window_, width = width_, height=height_, bg = 'lightblue')
    can.pack()
    return can

def pos(theta, theta_inc):
    theta_acc = -sin(theta)*g/length
    theta = theta + theta_inc * step
    theta_inc = theta_inc + theta_acc * step - theta_inc*fric*step
    return theta, theta_inc

def animation(canv):
    theta_n = theta0
    theta_inc_n = theta_inc0

    canv.create_oval((window_width/2-10, y0-10), (window_width/2+10, y0+10), fill = 'black', outline='brown')
    ball = canv.create_oval((window_width/2+ ceil(length*200*sin(theta_n))-15, y0+ceil(length*200*cos(theta_n))-15),
                            (window_width/2+ ceil(length*200*sin(theta_n))+15, y0+ceil(length*200*cos(theta_n))+15),
                            outline='red', fill = 'black', width=5)
    line = canv.create_line((window_width/2, y0), (window_width/2, y0+ceil(length*200)), width=5)

    while True:
        x = window_width/2 + ceil(length*200*sin(theta_n))
        y = y0+ ceil(length*200*cos(theta_n))
        theta_n, theta_inc_n = pos(theta_n, theta_inc_n)
        dx = window_width/2 + ceil(length*200*sin(theta_n)) - x
        dy = y0 + ceil(length*200*cos(theta_n)) - y
        canv.move(ball, dx, dy)
        canv.coords(line, window_width/2, y0,
                    window_width/2 + ceil(length*200*sin(theta_n)), y0+ ceil(length*200*cos(theta_n)))
        window.update()
        time.sleep(step)

window = create_window(window_width, window_height)
canvas = create_canvas(window, window_width, window_height)
animation(canvas)

theta_n = theta0
theta_inc_n = theta_inc0
for i in range(100):
    theta_n, theta_inc_n = pos(theta_n, theta_inc_n)
    print(theta_n, window_width/2 + ceil(length*200*sin(theta_n)), y0+ ceil(length*200*cos(theta_n)))
