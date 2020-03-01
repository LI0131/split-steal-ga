from random import random
from config import GENE_PROBABILITY


class Gene():

    def __init__(self):
        self.gene = self._create_gene()

    def get_value(self):
        return self.gene

    def _create_gene(self):
        return 1 if random() > GENE_PROBABILITY else 0

    def __repr__(self):
        return str(self.gene)

    def __iter__(self):
        yield self.gene