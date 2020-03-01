from random import randint, random
from config import (
    SELECTION_SIZE, ITERATIONS, DEEP_CROSSOVER_THRESHOLD,
    DEEP_MUTATION_THRESHOLD, CROSSOVER_THRESHOLD, MUTATION_THRESHOLD
)
from genome import Genome


class GeneticAlgorithm():

    def __init__(self, inital_pop):
        self.population = inital_pop

    def selection(self):

        def tournament(pool):
            index = 0
            while len(pool) > 1:
                x = 0
                y = 0
                for a, b in zip(pool[index], pool[index + 1]):
                    if a == 0 and b == 0:
                        x += 1
                        y += 1
                    elif a == 1 and b == 0:
                        x += 1
                    elif a == 0 and b == 1:
                        y += 1
                    else:
                        continue
                pool.pop(index) if x > y else pool.pop(index + 1)
            return pool[0]

        pool = []
        for _ in range(SELECTION_SIZE):
            pool.append(self.population[randint(0, len(self.population) - 1)])
        return tournament(pool)

    def __call__(self):
        for _ in range(ITERATIONS):
            winner = self.selection()
            for i in range(len(self.population)):
                prob = random()
                if prob > MUTATION_THRESHOLD and prob <= MUTATION_THRESHOLD + CROSSOVER_THRESHOLD:
                    self.population[i].mutate()
                elif prob > MUTATION_THRESHOLD + CROSSOVER_THRESHOLD and prob <= CROSSOVER_THRESHOLD + DEEP_MUTATION_THRESHOLD:
                    self.population[i].crossover(winner)
                elif prob > CROSSOVER_THRESHOLD + DEEP_MUTATION_THRESHOLD and prob <= DEEP_MUTATION_THRESHOLD + DEEP_CROSSOVER_THRESHOLD:
                    self.population[i].deep_mutation()
                else:
                    self.population[i].deep_crossover(winner)

            print(self.population.percent_one())