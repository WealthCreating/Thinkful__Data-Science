import random
import numpy as np


def get_max_and_remove(iterable):
    val = np.max(iterable)
    random_list.remove(val)
    return val

random_list = list(random.sample(range(100), 15))
max_val = get_max_and_remove(random_list)

tree = [max_val]
tree
tree.append([left, right])

for i in range(len(random_list)):
    left = get_max_and_remove(random_list)
    right = get_max_and_remove(random_list)
    tree[max_val] = (left, right)
