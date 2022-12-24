import random
turns_Easy =10
turn_Hard=5
turn_medium=7

def check_answer(a,b,t):
  if a==b:
    print(f"you guessed correctly the number was {b}")
  elif a>b:
    print("Too low")
    return t-1
  elif b>a:
    print("Too High")
    return t-1
    
def set_difficulty():
  X=input("choose a difficulty easy medium or hard :").lower()
  if X=='easy':
    return turns_Easy
  elif X=='medium':
    return turn_medium
  elif X=='hard':
    return turn_Hard
def game():  
  print("WELCOME TO GUESSING GAME")
  turns=set_difficulty()
  print("Computer has chose the number guess it")
  A=random.randint(1,100)
  B=0
  while B!=A:
    print(f"You have {turns} attempts remaining")
    B=int(input("Make a guess : "))
    turns =check_answer(A,B,turns)
    if turns==0:
      print("You ran out of turns")
      return

game()