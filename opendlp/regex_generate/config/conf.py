from enum import Enum,unique

@unique
class RegexFlavour(Enum):
    Java = 'Java'
    Python = 'Python'

BPE_PERCENT = 0.8
MAX_DEPTH = 7
POPULATION_SIZE = 2000
MAX_ITERATIONS = 1000

PRECISION_DIVIDE_CONQUER = 0.7
ITERATION_DIVIDE_CONQUER = int(MAX_ITERATIONS / 5)

NOISE_POSITIVE_SAMPLE_RATIO = 0.05