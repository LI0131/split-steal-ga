from random import randint, random
from statistics import mean
from chromosome import Chromosome
from config import GENOME_SIZE, GENOME_CROSSOVER_PROBABILITY


class Genome():

    def __init__(self):
        self.genome = self._create_genome()

    def _create_genome(self):
        return [Chromosome() for _ in range(GENOME_SIZE)]

    def percent_one(self):
        return mean([c.percent_one() for c in self.genome])

    def percent_zero(self):
        return mean([c.percent_zero() for c in self.genome])

    def crossover(self, other):
        split_point = randint(1, GENOME_SIZE - 2)
        if random() > GENOME_CROSSOVER_PROBABILITY:
            for i in range(split_point):
                self.genome[i] = other[i]
        else:
            for i in range(split_point, GENOME_SIZE - 1):
                self.genome[i] = other[i]

    def deep_crossover(self, other):
        for i in range(GENOME_SIZE):
            self.genome[i].crossover(other[i])

    def mutate(self):
        self.genome[randint(0, GENOME_SIZE - 1)] = Chromosome()

    def deep_mutation(self):
        for i in range(GENOME_SIZE):
            self.genome[i].mutate()

    def __repr__(self):
        return str(self.genome)

    def __len__(self):
        return len(self.genome)

    def __iter__(self):
        yield self.genome.__iter__()

    def __getitem__(self, index):
        return self.genome[index]

    def __setitem__(self, index, value):
        self.genome[index] = value