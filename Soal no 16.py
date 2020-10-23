max_number = 5
max_row = max_number * 2

for i in range (1, max_row):
  # print(i)
  number = ""
  max_column = i

  if max_column > max_number :
    max_column = max_number - (i - max_number)

  for j in range (1, max_row):
    # number = j
    if j <= max_column or j >= (max_row - max_column) :
      right_number = j

      if j > max_number :
        right_number = max_number - (j - max_number)

      number += str(right_number)
    else :
      number += " "
  
  print(number)