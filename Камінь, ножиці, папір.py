import random

def get_choices():
  player_choice = input("Зроби вибір (камінь, ножиці, папір): ")
  options = ["камінь", "папір", "ножиці"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"Ти обрав {player}, комп'ютер обрав {computer}")
  if player == computer:
    return "Нічия!"
  elif player == "камінь": 
    if computer == "ножиці":
      return "Камінь розбиває ножиці! Ти виграв!"
    else:
      return "Папір накриває камінь! Ти програв!"
  elif player == "папір":
    if computer == "камінь":
      return "Папір накриває камінь! Ти виграв!"
    else:
      return "Ножиці ріжуть папір! Ти програв! "
  elif player == "ножиці":
    if computer == "папір":
      return "Ножиці ріжуть папір! Ти виграв!"
    else:
      return "Камінь розбиває ножиці! Ти програв!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
