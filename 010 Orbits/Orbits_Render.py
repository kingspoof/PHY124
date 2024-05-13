GravitationalConstant = 6.67430e-11
LightSpeed = 2.99792458e8

class SolarSystem:
    def __init__(self, planets, dt):
        self.planets = planets
        self.time = 0
        self.dt = dt


    def update_acceleration(self):
        for p in self.planets: p.update_acceleration(self.planets)
    
    def update_velocity(self):
        for p in self.planets: p.update_velocity(self.dt)

    def update_position(self):
        for p in self.planets: p.update_position(self.dt)

    #returns the x coordinates as a list and the y coordinates as another list
    def get_coordinates(self):
        return [i[0] for i in self.positions], [i[1] for i in self.positions]

class Planet:
    def __init__(self, mass, start_position, start_velocity):
        #Change the values to a good value and not some arbitrary thing
        mass = mass / GravitationalConstant * LightSpeed**3
        start_position = [i * LightSpeed for i in start_position]
        start_velocity = [i * LightSpeed for i in start_velocity]

        self.mass = mass
        self.positions = [start_position]
        self.velocities = [start_velocity]
        self.acceleration = [[0,0]]
    
    def get_position(self):
        return self.positions[-1]

    # recalculate the acceleration based on the current position of the planets
    def update_acceleration(self, planets):
        resulting_acceleration = [0, 0]
        potential_energy = 0
        for planet in [p for p in planets if p is not self]:
            # calculate the distance between the two objects
            direction = [planet.get_position()[0] - self.get_position()[0], planet.get_position()[1] - self.get_position()[1]]
            distance = np.sqrt((direction[0])**2 + (direction[1])**2)
            direction_normalized = [i / distance for i in direction]


            force = self.mass * planet.mass * GravitationalConstant / distance**2
            acc = force / self.mass
            normalized_acceleration = [i * acc for i in direction_normalized]
            
            for i in range(len(resulting_acceleration)):
                resulting_acceleration[i] += normalized_acceleration[i]
        self.acceleration.append(resulting_acceleration)
    
    def update_velocity(self, timestep):
        self.velocities.append(
            [
                self.velocities[-1][0] + self.acceleration[-1][0] * timestep,
                self.velocities[-1][1] + self.acceleration[-1][1] * timestep,
            ]
        )

    #in this step, we also calculate the kinetic energy as well as the potential energy for this planet.
    def update_position(self, timestep):
        self.positions.append(
            [
                self.positions[-1][0] + self.velocities[-1][0] * timestep,
                self.positions[-1][1] + self.velocities[-1][1] * timestep
            ]
        ) 

def calculate_distance(pos1, pos2):
    distance_x = pos1[0] - pos2[0]
    distance_y = pos1[1] - pos2[1]
    distance = np.sqrt(distance_x**2 + distance_y**2)
    return distance