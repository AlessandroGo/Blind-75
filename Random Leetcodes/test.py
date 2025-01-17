def TreeConstructor(strArr):
  hashMap = {}
  for tup in strArr:
    if tup[3] not in hashMap:
      hashMap[tup[3]] = 1
      continue
    if tup[3] in hashMap:
      hashMap[tup[3]] += 1
    if hashMap[tup[3]] > 2:
      print(hashMap)
      return False
  # code goes here
  print(hashMap)
  return True

print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))

numbers = [1, 2, 3, 4, 5, 6]

# Using list comprehension with a condition
hashmap = {num: num**2 for num in numbers}

print(hashmap)