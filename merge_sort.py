import random
from sorting import less, exchange, check

def merge_sort(array, lo, hi):
  if hi <= lo:
    return

  mid = lo + (hi - lo) // 2

  merge_sort(array, lo, mid)
  merge_sort(array, mid + 1, hi)

  merge(array, lo, mid, hi)


def merge(array, lo, mid, hi):
  # copy entries to auxiliary to help merge
  auxiliary = list(array)
  
  # need 3 index i, j, k to merge
  i, j = lo, mid + 1
  for k in range(lo, hi + 1):
    if i > mid:
      array[k] = auxiliary[j]
      j = j + 1
    elif j > hi:
      array[k] = auxiliary[i]
      i = i + 1 
    elif auxiliary[j] < auxiliary[i]:
      array[k] = auxiliary[j]
      j = j + 1
    else:
      array[k] = auxiliary[i]
      i = i + 1 


array = [random.randint(0,20) for i in range(0, 12)]
print(array)
merge_sort(array, 0, len(array) - 1)
print(array)

