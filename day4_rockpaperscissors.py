import random

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
choices = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")
selection = input("Select Rock, Paper, or Scissors: ")
selection_lower = selection.lower()

if  selection_lower == 'rock':
    print(f"You: {rock}")
if selection_lower == 'paper':
    print(f"You: {paper}")
if selection_lower == 'scissors':
    print(f"You: {scissors}")

random_choice = random.choice(choices)

if selection_lower == 'rock' and random_choice == choices[0]:
    print(f"Opponent: {random_choice}")
    print("Its a draw")
if selection_lower == 'rock' and random_choice == choices[1]:
    print(f"Opponent: {random_choice}")
    print("You lost!")
if selection_lower == 'rock' and random_choice == choices[2]:
    print(f"Opponent: {random_choice}")
    print("You won!")

if selection_lower == 'paper' and random_choice == choices[0]:
    print(f"Opponent: {random_choice}")
    print("You Won!")
if selection_lower == 'paper' and random_choice == choices[1]:
    print(f"Opponent: {random_choice}")
    print("Its a draw")
if selection_lower == 'paper' and random_choice == choices[2]:
    print(f"Opponent: {random_choice}")
    print("You lost!")

if selection_lower == 'scissors' and random_choice == choices[0]:
    print(f"Opponent: {random_choice}")
    print("You lost!")
if selection_lower == 'scissors' and random_choice == choices[1]:
    print(f"Opponent: {random_choice}")
    print("You Won!")
if selection_lower == 'scissors' and random_choice == choices[2]:
    print(f"Opponent: {random_choice}")
    print("Its a draw")
