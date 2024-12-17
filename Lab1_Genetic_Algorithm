import random

# Genetic Algorithm Parameters
POPULATION_SIZE = 20
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
NUM_GENERATIONS = 50
RANGE_MIN = -10
RANGE_MAX = 10

# Objective function to maximize
def fitness_function(x):
    return x**2

# Create an initial population of random individuals within the specified range
def create_initial_population():
    return [random.uniform(RANGE_MIN, RANGE_MAX) for _ in range(POPULATION_SIZE)]

# Evaluate the fitness of each individual in the population
def evaluate_population(population):
    return [fitness_function(individual) for individual in population]

# Select two parents based on their fitness using roulette wheel selection
def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    if total_fitness == 0:
        return random.choice(population), random.choice(population)

    selection_probs = [fitness / total_fitness for fitness in fitness_scores]
    parent1 = random.choices(population, weights=selection_probs, k=1)[0]
    parent2 = random.choices(population, weights=selection_probs, k=1)[0]
    return parent1, parent2

# Perform crossover between two parents to create offspring
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        alpha = random.random()
        offspring1 = alpha * parent1 + (1 - alpha) * parent2
        offspring2 = alpha * parent2 + (1 - alpha) * parent1
        return offspring1, offspring2
    return parent1, parent2

# Apply mutation to an individual
def mutate(individual):
    if random.random() < MUTATION_RATE:
        return random.uniform(RANGE_MIN, RANGE_MAX)
    return individual

# Genetic Algorithm main loop
def genetic_algorithm():
    # Initialize population
    population = create_initial_population()

    # Track the best solution
    best_solution = None
    best_fitness = float('-inf')

    # Run for a specified number of generations
    for generation in range(NUM_GENERATIONS):
        # Evaluate the fitness of the population
        fitness_scores = evaluate_population(population)

        # Update the best solution
        for i in range(POPULATION_SIZE):
            if fitness_scores[i] > best_fitness:
                best_fitness = fitness_scores[i]
                best_solution = population[i]

        # Create a new population
        new_population = []

        # Perform selection, crossover, and mutation to generate new individuals
        while len(new_population) < POPULATION_SIZE:
            # Select parents
            parent1, parent2 = select_parents(population, fitness_scores)

            # Perform crossover
            offspring1, offspring2 = crossover(parent1, parent2)

            # Apply mutation
            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)

            # Add offspring to the new population
            new_population.extend([offspring1, offspring2])

        # Replace the old population with the new population
        population = new_population[:POPULATION_SIZE]

        # Output progress
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Best Solution = {best_solution}")

    # Output the best solution found
    print("\nBest Solution Found:")
    print(f"x = {best_solution}, f(x) = {best_fitness}")

# Run the Genetic Algorithm
genetic_algorithm()
