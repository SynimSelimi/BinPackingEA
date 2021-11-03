import random

population_size = 100
number_of_bins = 5
number_of_items = 10
item_limit_size = 35
max_weight = 50
items = [20, 27, 2, 14, 26, 15, 17, 13, 5, 4]
# items = [random.randrange(1, item_limit_size) for _ in range(number_of_items)]

print("bins:", number_of_bins, "|_| " * number_of_bins)
print("bin capacity:", max_weight)
print("items:", items)

def print_population(_pop):
    for row in _pop:
        print("items:", *row, "bins:", measure_bins(row))

def measure_bins(solution):
    bins = [0] * number_of_bins
    for item, bin in enumerate(solution):
        bins[bin - 1] += items[item]
        
    return bins

def find_a_solution():
    bins = [i for i in range(1, number_of_bins + 1)]
    bin_items = items.copy()
    random.shuffle(bin_items)
    random.shuffle(bins)
    solution = [0] * number_of_items

    item = 0
    sum = 0
    bin = bins.pop()
    while len(bin_items) > 0:
        weight = bin_items.pop()
        sum += weight
        if sum <= max_weight:
            index = items.index(weight)
            solution[index] = bin
            item += 1
        else:
            bin_items.append(weight)
            bin = bins.pop()
            sum = 0
    
    return solution

def main():
    population = []
    if sum(items) > number_of_bins * max_weight:
        print("Cannot fit all items in bins")
        return

    while (len(population) < population_size):
        solution = find_a_solution()
        if solution not in population:
            population.append(solution)
            
    print_population(population)
    
main()
