from numpy import random

string = ["Rock", "Paper", "Scissor"]
computer_marks=0
user_marks=0

def computer():
    co = random.choice(string)
    return co.upper()

def user():
    choice = input("Enter your choice (Rock/Paper/Scissor): ").strip().upper()
    while choice not in ["ROCK", "PAPER", "SCISSOR"]:
        choice = input("Invalid choice! Please enter Rock, Paper, or Scissor: ").strip().upper()
    return choice

def result(comp, user):
    global computer_marks, user_marks
    if comp == user:
        return "It's a Tie!"
    elif (comp == "ROCK" and user == "SCISSOR") or (comp == "PAPER" and user == "ROCK") or (comp == "SCISSOR" and user == "PAPER"):
        computer_marks +=1
        return f"Computer: {computer_marks} User: {user_marks} "
    else:
        user_marks +=1
        return f"Computer: {computer_marks} User: {user_marks} "
    
def final_result(user_name):
    if computer_marks > user_marks:
        return " TINSON Wins the Game!"
    elif user_marks > computer_marks:
        return f"{user_name} Wins the Game!"
    else:
        return "The Game is a Tie!"