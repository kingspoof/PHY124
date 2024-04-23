import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

gamma = 0.25
lamda = 0.075
l = 0.4

def a_phi(o, tau):
    return -1 *gamma * (np.sin(o)) - lamda * np.sin(0 - tau)


def calculate_phi(start_phi, max_time):
    phi = [start_phi]
    v_phi = [0]
    dtau = 0.01 * 2 * np.pi
    tau = [0]
    depth = 2
    while tau[-1] < (max_time * 2 * np.pi) - dtau/2:
        for i in range(depth):
            # update the time step 
            tau.append(tau[-1] + dtau/depth)
            #update the position
            phi.append(phi[-1] + v_phi[-1] * dtau/depth)

            if(i != range(depth)[-1]):
                #update the velocity    
                v_phi.append(v_phi[-1] + a_phi(phi[-1], tau[-1]))
    return phi, tau


phis = [
    calculate_phi(np.pi/4, 50),
    #calculate_phi(np.pi),
    calculate_phi(-np.pi/4, 50)
]
colors = [
    'red', 'blue', 'orange'
]

time = [t/np.pi * 2 for t in phis[0][1]]
def update(frame):
    frame+= 50
    ax.clear()
    ax.set_facecolor(plt.cm.Blues(.2))
    #ax.set_ylim([-np.pi/2, np.pi/2])
    ax.set_ylim([-2, 2])

    for i in range(len(phis)):
        ax.scatter(
            time[0 if frame <= 60 else frame-60:frame],
            phis[i][0][0 if frame <= 60 else frame-60:frame], 
            c=colors[i],
        )


#fig, ax = plt.subplots(figsize=(6,6))
#anime = FuncAnimation(
#    fig = fig, 
#    func = update,
#    frames = len(phis[0][1]),
#    interval = 48
#)
#plt.xlabel('Time interval (s)')
#plt.ylabel('Angle (respective to the horizontal)')
#plt.legend()
#plt.show()


import pygame
from pygame.locals import *
pygame.init()


BACKGROUND = (255, 255, 255)

fps = 24
fpsClock = pygame.time.Clock()
height = (500, 500)

window = pygame.display.set_mode(height)


def circle(position, radius, color):
    pygame.draw.circle(window, color, position, radius)



def main():
    looping = True
    
    
    time = 0
    time_max = 60 * 100
    phi, tau = calculate_phi(0, time_max)
    #tau = [t/(2*np.pi) for t in tau]



    while looping:
        for event in pygame.event.get():
            if QUIT == event.type:
                pygame.quit()
                sys.exit()
        
        print(phi[time], tau[time])

        #processing

        window.fill(BACKGROUND)
        circle([250, 250], 30, (0,0,0))
        circle([250, 250], 25, (255, 255, 255))


        p = [250 + (np.cos(gamma * tau[time])*27.5), 250 + np.sin(gamma * tau[time])*27.5]
        circle(p, 5, (255, 0, 0))
        #calculate the position of the pendulum
        pendulum = [p[1] -l*100*np.cos(phi[time]), p[0] + l*100 * np.sin(phi[time])]
        print('pendulum', pendulum)
        circle(pendulum, 5, [0, 255, 255])


        time = time + 1
        print(time)




        pygame.display.update()
        fpsClock.tick(fps)


main()


