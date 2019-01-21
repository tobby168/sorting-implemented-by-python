import random
from sorting import less, exchange, check

def insertion_sort(array):
  for i in range(len(array)):
    for j in range(i, 0, -1):
      if less(array[j], array[j - 1]):
        exchange(array, j, j - 1)
      else:
        break


"""
array = [random.randint(0,10) for i in range(0, 10)]
print(array)
insertion_sort(array)
print(array)
"""