import random

# Define the fitness function (example: Sphere function)
def fitness_function(position):
    return sum([x**2 for x in position])

# Particle class to represent each particle
class Particle:
    def __init__(self, dimensions):
        self.position = [random.uniform(-10, 10) for _ in range(dimensions)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dimensions)]
        self.best_position = list(self.position)
        self.best_fitness = fitness_function(self.position)

    def update_velocity(self, global_best_position, inertia, cognitive, social):
        for i in range(len(self.position)):
            inertia_component = inertia * self.velocity[i]
            cognitive_component = cognitive * random.random() * (self.best_position[i] - self.position[i])
            social_component = social * random.random() * (global_best_position[i] - self.position[i])
            self.velocity[i] = inertia_component + cognitive_component + social_component

    def update_position(self):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

# PSO function
def particle_swarm_optimization(fitness_function, dimensions, num_particles, max_iterations):
    particles = [Particle(dimensions) for _ in range(num_particles)]
    global_best_position = particles[0].position
    global_best_fitness = fitness_function(global_best_position)

    for _ in range(max_iterations):
        for particle in particles:
            fitness = fitness_function(particle.position)

            # Update personal best
            if fitness < particle.best_fitness:
                particle.best_position = list(particle.position)
                particle.best_fitness = fitness

            # Update global best
            if fitness < global_best_fitness:
                global_best_position = list(particle.position)
                global_best_fitness = fitness

        for particle in particles:
            particle.update_velocity(global_best_position, inertia=0.5, cognitive=1.5, social=1.5)
            particle.update_position()

    return global_best_position, global_best_fitness

# Parameters
dimensions = 2
num_particles = 30
max_iterations = 100

# Run PSO
best_position, best_fitness = particle_swarm_optimization(fitness_function, dimensions, num_particles, max_iterations)

print("Best Position:", best_position)
print("Best Fitness:", best_fitness)
