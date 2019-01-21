import random
from sorting import less, exchange, check

def selection_sort(array):
  for i in range(len(array)):
    exchange(array, i, array.index(min(array[i:]), i))


"""
array = [round(random.random() * 10) for i in range(0, 10)]
print(array)
selection_sort(array)
print(array)
"""