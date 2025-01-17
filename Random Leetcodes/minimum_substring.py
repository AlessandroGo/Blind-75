def MinWindowSubstring(strArr):
  pointer1 = 0
  pointer2 = 0
  firstMap = {}
  secondMap = {}
  have_unique_greater_or_equal = 0
  minimumLength = float("infinity")
  # If all second map values are greater than or equal then it is a substring i.e. #aaabc of N for #abc of K
  for char in strArr[1]:
    if char not in secondMap:
      secondMap[char] = 1
    else:
      secondMap[char] += 1
  for char in strArr[1]:
    firstMap[char] = firstMap.get(char,0)
  # Initialize here or it will be 0
  need_equal = len(secondMap)

  for char in strArr[0]:
    if char in secondMap:
      firstMap[char] += 1
      # After updating N's map, if we see that firstMap's count of that char is same K's count we increment have_unique
      # i.e. if firstmap's -> {"a" : 4} and secondMap's -> {"a" : 2} it is a 1 if {"a" : 1} and {"a" : 2} then is it 0 
      # remember we need have_unique to be same as length of secondMap to realize a substring
      if firstMap[char] == secondMap[char]:
        have_unique_greater_or_equal += 1
    # Regardless of if char in K we move to right
    pointer2 += 1
    # If this is executed we have realised a valid substring
    while have_unique_greater_or_equal == need_equal:
      # Only update substring of N if it is less than current substring of N
      if (pointer2 - pointer1 + 1) < minimumLength:
        minimumLength = pointer2 - pointer1 + 1
        # It will be from pointer 1 to pointer2 -1 - how python slicing works
        subString = strArr[0][pointer1:pointer2]
      # Pop from left
      char = strArr[0][pointer1]
      if char in secondMap and (firstMap[char] - 1) < secondMap[char]:
        firstMap[char] -= 1
        have_unique_greater_or_equal -= 1
        pointer1 += 1
        # without continue statement the below if char in firstMap will execute and it will double decrement the value
        # Also dont want to update left pointer because then it is no longer a valid substring
        continue
      if char in firstMap:
        firstMap[char] -= 1
      # In all cases of the while loop we will move left pointer up one to the right to minimise the window
      pointer1 += 1
      
  # code goes here
  return subString

# keep this function call here 
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))