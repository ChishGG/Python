import random
comp_options = ["rock", "paper", "scissors"]
comp_choice = random.choice(comp_options)
user_choice = input("Rock, Paper, Scissors! ")

if user_choice.lower() == 'rock' and comp_choice == 'paper' :
  print(comp_choice)
  print("Comp Won")
elif user_choice.lower() == 'paper' and comp_choice == 'scissors' :
  print(comp_choice)
  print("Comp Won")
elif user_choice.lower() == 'scissors' and comp_choice == 'rock' :
  print(comp_choice)
  print("Comp Won")
elif user_choice.lower() == 'rock' and comp_choice == 'scissors' :
  print(comp_choice)
  print("You Won")
elif user_choice.lower() == 'paper' and comp_choice == 'rock' :
  print(comp_choice)
  print("You Won")
elif user_choice.lower() == 'scissors' and comp_choice == 'paper' :
  print(comp_choice)
  print("You Won")
elif user_choice.lower() == comp_choice.lower():
  print("Draw")
else:
  print("wrong choice!")
