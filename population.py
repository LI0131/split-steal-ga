from statistics import mean
from genome import Genome
from config import POPUALATION_SIZE


class Population():

    def __init__(self):
        self.pop = self._create_population()

    def _create_population(self):
        return [Genome() for _ in range(POPUALATION_SIZE)]

    def percent_one(self):
        return mean([c.percent_one() for c in self.pop])

    def percent_zero(self):
        return mean([c.percent_zero() for c in self.pop])

    def get_uniqueness(self):
        pass

    def __repr__(self):
        return str(self.pop)

    def __iter__(self):
        yield self.pop.__iter__()

    def __len__(self):
        return len(self.pop)

    def __getitem__(self, index):
        return self.pop[index]

    def __setitem__(self, index, value):
        self.pop[index] = value