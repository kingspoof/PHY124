import sympy as sy
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from numpy import cos, sin, arccos, linspace

r = sy.Symbol('r')
p_r = sy.Symbol('p_r')
p_phi = sy.Symbol('p_phi')


state = [0,0,0]
def evaluate_state(state):
    return state[0], state[1], state[2], state[3]

def pack_state(r, phi, dp_r, dp_phi):
    return [r, phi, dp_r, dp_phi]



def ode(state, t):
    r, phi, p_r, p_phi = evaluate_state(state)
    drdt = (1 - 2/r)*p_r
    dphidt = p_phi/(r**2)
    dp_rdt = -(p_r**2/r**2) + (p_phi**2 / r**3) - (1/(r-2)**2)
    dp_phidt = 0
    return pack_state(drdt, dphidt, dp_rdt, dp_phidt)




r_init = 190
time_max = 11198
base_state = pack_state(r_init, 0, 0, (r_init**(3/2)/(r_init - 2)**(1/2)))
time = linspace(0, time_max, 1000)
print((r_init**(3/2)/(r_init - 2)))

#solution = odeint(ode, base_state, time)


#import pygame, sys
#from pygame.locals import *
#pygame.init()

#width = 800
#height = 800

#fpsClock = pygame.time.Clock()
#window = pygame.display.set_mode((width, height))



def calc_pos(r, phi):
    return width / 2 + r * cos(phi), height / 2 + r * sin(phi) 

def main():
    return
    looping = True    
    states = [base_state]
    while looping:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        window.fill((0,0,0))
        
        states.append(odeint(ode, states[-1], [0,1])[-1])

        pygame.draw.circle(window, (0, 255, 0), (calc_pos(states[-1][0], states[-1][1])), 5)
        pygame.draw.circle(window, (255,255,255), (width/2, height/2), 5)


        first = True
        last_state = None
        for state in states:
            if first:
                last_state = state
                first = False
                continue

            pos1 = calc_pos(last_state[0], last_state[1])
            pos2 = calc_pos(state[0], state[1])
            pygame.draw.line(window, (200, 200, 200), pos1, pos2, 1)
            last_state = state




        pygame.display.update()
        fpsClock.tick(50)


#main()


result = odeint(ode, base_state, time)
x = []
for res in result:
    x.append(res[1] - arccos(r_init / res[0]))


plt.plot(time, x)
plt.show()