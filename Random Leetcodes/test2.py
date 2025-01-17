def QuestionsMarks(strParam):
  match_found = True
  last_number = 0
  question_count = 0 
  for c in strParam:
    if c.isdigit():
      if int(c) + last_number == 10 and question_count == 3:
        match_found = True
      elif int(c) + last_number == 10 and question_count != 3:
        return False
      last_number = int(c)
      question_count = 0
    elif c == "?":
      question_count += 1
  # code goes here
  return match_found

# keep this function call here 
print(QuestionsMarks("aa6?9"))