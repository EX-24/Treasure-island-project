print("Welcome To Tresure Island.")
print("Your Mission is to Find The Tresure.")
choice1=input('you\'r at crossroad. Where do you want to go ? type "right" or "left".').lower()

if choice1 == "left":
  choice2 = input('you want "swim" or "wait".')
  if choice2 == "swim":
    print("game over")
  elif choice2 =="wait":
    door = input('which color door you want "red", "yellow",or "blue".').lower()
    if door == "red" or door== "blue":
      print("game over")
    else:
      print("you win!")
else:
  print("game over")