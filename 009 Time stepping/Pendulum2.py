import numpy as np
from numpy import pi, sin, cos, sqrt
import pygame, sys, random
from pygame.locals import *
pygame.init()


# Setup for the variables
g = 10
L = 0.1
l = 0.4
ohm = 10
omega = sqrt(g/l)
gamma = omega**2/ohm**2
lamda = L / l

#Setup for pygame
background = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (255, 255, 255)
fps = 50
fpsClock = pygame.time.Clock()
width = 800
height = 800
multiplier = 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pendulum Simulation')

def a(phi, tau):
    return -1 * gamma * sin(phi) - lamda * sin(phi - tau)


pendulas = []
for i in range(1000):
    pendulas.append({
        'phi': [pi/2 + i*0.0001],
        'v_phi': [0],
        'pos': [],
        'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    })

def main():
    time = [0]
    dt = 1/100
    dtau = dt * 2 * pi
    looping = True
    tau = [0]


    while looping:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        window.fill(background)

        #increate tau
        tau.append(tau[-1] + dtau)

        rotary_pos = (width/2, height/2)
        #draw the rotary thingy
        pygame.draw.circle(window, (150, 150, 150), rotary_pos, L * multiplier)
        pygame.draw.circle(window, background, rotary_pos, (L-0.005)*multiplier)

        #draw the point, where the rotary thingy is attached
        attatched_position = (
            rotary_pos[0] + L*multiplier*sin(tau[-1]), 
            rotary_pos[1] + L*multiplier*cos(tau[-1])
            )
        #pygame.draw.circle(window, red, attatched_position, 2)



        #here we calculate the next position for phi
        for p in pendulas:
            p['phi'].append(p['phi'][-1] + p['v_phi'][-1] * dtau)
            p['v_phi'].append(p['v_phi'][-1] + a(p['phi'][-1], tau[-1]) * dtau)

        #now we can draw the pendulum thingy
        for p in pendulas:
            p['pos'].append((
                    attatched_position[0] + sin(p['phi'][-1]) * l * multiplier,
                    attatched_position[1] + cos(p['phi'][-1]) * l * multiplier
                ))

        for p in pendulas:
            pygame.draw.line(window, (150, 150, 150), attatched_position, p['pos'][-1], 2)

            
        for p in pendulas:
            points = 50
            for i in range(0 if len(p['pos']) < points else len(p['pos']) - points, len(p['pos'])-1):
                cd = i/len(p['pos'])
                pygame.draw.line(window, (cd * p['color'][0], p['color'][1], p['color'][2]), p['pos'][i], p['pos'][i+1], 1)
        

        
        for p in pendulas:
            #here we draw the pendulum, such that it is always on top
            pygame.draw.circle(window, p['color'], p['pos'][-1], 8)

        pygame.display.update()
        fpsClock.tick(fps)


main()