import random
from sorting import less, exchange, check

def quick_sort(array):
  # shuffle the array is needed to ensure the runtime
  random.shuffle(array)
  sort(array, 0, len(array) - 1)

def sort(array, lo, hi):
  if hi <= lo:
    return
  
  # sort the array recursively
  j = partition(array, lo, hi)
  sort(array, lo, j - 1)
  sort(array, j + 1, hi)


def partition(array, lo, hi):
  i = lo
  j = hi + 1

  while True:

    # find entry from left to swap
    while less(array[i + 1], array[lo]):
      i = i + 1
      if i == hi:
        break
    # the index to swap
    i = i + 1

    # find entry from right to swap
    while less(array[lo], array[j - 1]):
      j = j - 1
      if j == lo:
        break
    # the index to swap
    j = j - 1

    # check if pointers cross
    if i >= j:
      break
    
    # swap
    exchange(array, i, j)

  # put the partition item to the right place
  exchange(array, lo, j)
  # return index of partition item
  return j



array = [random.randint(0,20) for i in range(0, 12)]
print(array)
quick_sort(array)
print(array)

