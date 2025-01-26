import random

class ascii:

  def __init__(self):

    self.r='''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    self.p='''
        _______
    ---'   ____)____
              ______)
              _______)
            _______)
    ---.__________)
    '''

    self.s='''
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    '''
    self.rm='''
     _______
    (____   '---
   (_____)
   (_____)
    (____)
     (___)__.---

    '''
    self.pm='''
           _______
      ____(____   '---
     (______)
    (_______
     (_______
       (__________.---
    '''

    self.sm='''
         _______
    ____(____   '---
   (______)
   (__________
        (____)
         (___)__.---
    '''


class rock_paper_scissors(ascii):
  def compare(self,a,b):
    if a=='rock':
      user_choice=self.r
    elif a=='paper':
      user_choice=self.p
    elif a=='scissors':
      user_choice=self.s
    else:
      print("Invalid choice")

    if b=='rock':
      computer_choice=self.rm
    elif b=='paper':
      computer_choice=self.pm
    elif b=='scissors':
      computer_choice=self.sm
    else:
      print("Invalid choice")

    print(f"Your choice : {user_choice} \nComputer choice : {computer_choice}")
    if a==b:
      print("It's a tie")
    elif a=='rock' and b=='scissors':
      print("You win")
    elif a=='paper' and b=='rock':
      print("You win")
    elif a=='scissors' and b=='paper':
      print("You win")
    else:
      print("You lose")


choice=['rock','paper','scissors']

game=rock_paper_scissors()

while True:

  user_choice=input("Enter your choice (rock,paper,scissors,quit) : ")
  computer_choice=random.choice(choice)

  match user_choice.lower():
    case 'rock':
      game.compare(user_choice.lower(),computer_choice)
    case 'paper':
      game.compare(user_choice.lower(),computer_choice)
    case 'scissors':
      game.compare(user_choice.lower(),computer_choice)
    case 'quit':
      print("Thanks for playing, Have a nice day :)")
      break
    case _:
      print("Invalid choice")
