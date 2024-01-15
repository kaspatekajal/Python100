rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)

random_choice = random.randint(0,2)
if random_choice == 0:
  print(rock)
elif random_choice == 1:
  print(paper)
elif random_choice == 2:
  print(scissors)

if user_choice == 0 and random_choice == 2:
  print("You win")
elif user_choice == 1 and random_choice == 0:
  print("You win")
elif user_choice == 2 and random_choice == 1:
  print("You win")
elif user_choice == random_choice:
  print("It's a draw")
elif user_choice > 2:
  print("You typed an invalid number, you lose!")
else:
  print("You lose")
