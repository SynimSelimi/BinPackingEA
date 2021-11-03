import random
import itertools
 
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

population_size = 100
number_of_bins = 5
number_of_items = 10
item_limit_size = 50
max_weight = 50

bins = [0] * number_of_bins
items = {random.randrange(1, item_limit_size) for i in range(number_of_items)}

population = []
while (len(population) < population_size):
    subsets = findsubsets(items, 2)
    for subset in subsets:
        if sum(subset) < max_weight:
            population.append(subset)
    
print(population)
