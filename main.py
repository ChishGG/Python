import random as rd

def compwins(x, y):
   if (x.lower() == 'rock' and y == 'paper'):
      return True
   elif (x.lower() == 'paper' and y == 'scissors'):
      return True
   elif (x.lower() == 'scissors' and y == 'rock'):
      return True

def userwins(x, y):
   if (x.lower() == 'rock' and comp_choice == 'scissors'):
      return True
   elif (x.lower() == 'paper' and comp_choice == 'rock'):
      return True
   elif (x.lower() =='scissors' and comp_choice == 'paper'):
      return True
    
comp_opt = ["rock","paper","scissors"]
comp_choice = rd.choice(comp_opt)
    
user_choice = input("\nRock, Paper, Scissors! ")

if compwins(user_choice, comp_choice) == True:
   print(comp_choice)
   print("Comp Won!\n")
elif userwins(user_choice, comp_choice) == True:
   print(comp_choice)
   print("You Won\n")
elif comp_choice == user_choice:
   print(comp_choice)
   print("Draw\n")
