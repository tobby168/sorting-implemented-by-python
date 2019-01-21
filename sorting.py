def compare(one, another):
  if one > another:
    return 1
  elif one < another:
    return -1
  else:
    return 0

def less(one, another):
  if compare(one, another) == -1:
    return True
  else:
    return False

def exchange(array, idx1, idx2):
  temp = array[idx1]
  array[idx1] = array[idx2]
  array[idx2] = temp
  return

def check(array):
  for i in range(1, len(array)):
    if less(array[i], array[i - 1]):
      return False
  return True