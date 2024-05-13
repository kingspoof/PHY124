import time
import math
import numpy as np
import json
from numpy import pi, cos, sin, sqrt
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta

img = plt.imread('data/World.jpg')
height = len(img)
width = len(img[0])

def Rx(angle): return np.array([[1, 0, 0], [0, cos(angle), sin(angle)], [0, -sin(angle), cos(angle)]])
def Ry(angle): return np.array([[cos(angle), 0, -sin(angle)], [0,1,0], [sin(angle), 0, cos(angle)]])
def Rz(angle): return np.array([[cos(angle), sin(angle), 0], [-sin(angle), cos(angle), 0], [0,0,1]])


# latitude and longitude given in degrees,
# date given in days
# time given in seconds
ex = np.array([1,0,0])
beta_base = 2*pi/(365)
l = 23.5 / 180 * pi
def daylight(latitude, longitude, date, time):
    beta = beta_base * date

    e1 = np.matmul(ex, np.matmul(Rz(beta), Rx(-l)))
    e2 = np.matmul(ex, np.matmul(Ry(latitude), Rz(longitude + (time * 2*pi/(24*60*60)) + beta)))

    return np.dot(e1, e2)


# function to render a single scene, returns a 2d array
def render_scene(date, time):
    longitude = np.linspace(-pi, pi, width)
    latitude = np.linspace(-pi/2, pi/2, height)

    height_map = [[0 for i in longitude] for i in latitude]
    for h, lat in enumerate(latitude):
        for w, long in enumerate(longitude):
            height_map[h][w] = daylight(lat, long, date, time)
    return height_map



def increment_date():
    date = datetime.strptime(date, '%d.%m.%Y')
    date += timedelta(days=1)
    date = date.strftime('%d.%m.%Y')

def animate(frame):
    frame *= 2
    print('starting rendering')
    plt.clf()
    plt.imshow(img)
    plt.contourf(render_scene(frame,0))
    print('ending rendering')

# calculate the stuff, so we can look at it from a better perspective
values = {}
file_path = 'data/calculation.json'
read_only = True

if(not read_only):
    for day in range(365):
        values[day] = render_scene(day, 0)
        print('rendered day: ' + str(day))

    # now we save tha values
    with open(file_path, 'w') as f:
        json.dump(values, f)
else:
    print('reading file')
    with open(file_path, 'r') as f:
        values = json.load(f)
    print('done reading file')






date = '30.08.2023'
def animate(frame):
    key = list(values.keys())[frame]
    plt.clf()
    plt.imshow(img)
    plt.contourf(values[key], alpha=0.4, levels=[-1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    #increment_date()
    #plt.title("Date: " + date)

ani = FuncAnimation(plt.gcf(), animate, frames=range(len(values)), interval=30/1000)
plt.show()