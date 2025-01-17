def CodelandUsernameValidation(strParam):
  if strParam[-1] == "_":
    return False
  if not strParam[0].isalpha():
    return False
  length = len(strParam)
  if length < 4 or length > 25:
    return False
  for c in strParam:
    if not (c.isalnum() or c == "_"):
      return False
  # code goes here
  return True

# keep this function call here 
print(CodelandUsernameValidation("u__hello_world123"))