# initially
missionary_on_right = 3
missionary_on_left = 0
cannibals_on_right = 3
cannibals_on_left = 0
boat_side = '----(__)'

# game conditions
def check_win():
  if missionary_on_right < cannibals_on_right and missionary_on_right>0:
    print("Game over")
    return True
  elif missionary_on_left < cannibals_on_left and missionary_on_left>0:
    print("Game over")
    return True
  elif cannibals_on_left == 3 and missionary_on_left == 3:
    print("Win")
    return True
  return False


print("m:",missionary_on_left," c:",cannibals_on_left, boat_side , "m:",missionary_on_right," c:",cannibals_on_right )
while True:
  # user input
  missionary = int(input("Enter no of missionary on boat: "))
  cannibals = int(input("Enter no of cannibals on boat: "))

  # input conditions
  if missionary + cannibals > 2 or missionary + cannibals <= 0:
    print("Invalid Input!")
    continue

  if boat_side == '----(__)':
    if missionary > missionary_on_right or cannibals > cannibals_on_right:
      print("Invalid Input")
      continue
    else:
      # boat travel right to left
      missionary_on_right -= missionary
      cannibals_on_right -= cannibals
      missionary_on_left += missionary
      cannibals_on_left += cannibals
      boat_side = '(__)----'
      if check_win():
        break

  else:
    if missionary > missionary_on_left or cannibals > cannibals_on_left:
      print("Invalid Input")
      continue
    else:
      # boat travel left to right
      missionary_on_right += missionary
      cannibals_on_right += cannibals
      missionary_on_left -= missionary
      cannibals_on_left -= cannibals
      boat_side = '----(__)'
      if check_win():
        break

  print("m:",missionary_on_left," c:",cannibals_on_left, boat_side , "m:",missionary_on_right," c:",cannibals_on_right )




