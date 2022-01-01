import numpy as np
from itertools import product
with open("./day11/data.txt") as input:
    raw_data = input.read().strip().split()
data = np.array([[int(x) for x in list(i)]for i in raw_data], dtype=int)
np.zeros


def pprint(arr):
    for line in arr:
        print("".join(str(i).ljust(3) for i in line))


pprint(data)
