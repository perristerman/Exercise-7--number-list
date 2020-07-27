list = (1, 2, 3, 4, 5)
playernumber = input("Pick a number 1-5 ")
playernumber = float(playernumber)
if playernumber == 1:
  print("There are no numbers less than 1")
elif playernumber == 2:
  print("There is 1 number less than 2")
elif playernumber == 3:
  print("There are 2 numbers less than 3")
elif playernumber == 4:
  print("There are 3 numbers less than 4")
else:
  print("There are 4 numbers less than 5")