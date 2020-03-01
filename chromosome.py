from random import randint, random
from gene import Gene
from config import CHROMOSOME_SIZE, CHROMOSOME_CROSSOVER_PROBABILITY


class Chromosome():

    def __init__(self):
        self.chromosome = self._create_chromosome()

    def _create_chromosome(self):
        return [Gene() for _ in range(CHROMOSOME_SIZE)]

    def percent_one(self):
        return sum([g.get_value() for g in self.chromosome]) / CHROMOSOME_SIZE

    def percent_zero(self):
        return (CHROMOSOME_SIZE - sum([g.get_value() for g in self.chromosome])) / CHROMOSOME_SIZE

    def crossover(self, other):
        split_point = randint(1, CHROMOSOME_SIZE - 2)
        if random() > CHROMOSOME_CROSSOVER_PROBABILITY:
            for i in range(split_point):
                self.chromosome[i] = other[i]
        else:
            for i in range(split_point, CHROMOSOME_SIZE - 1):
                self.chromosome[i] = other[i]

    def mutate(self):
        self.chromosome[randint(0, CHROMOSOME_SIZE - 1)] = Gene()

    def __repr__(self):
        return str(self.chromosome)

    def __iter__(self):
        yield self.chromosome.__iter__()

    def __getitem__(self, index):
        return self.chromosome[index]

    def __setitem__(self, index, value):
        self.chromosome[index] = value