import random
choices=["rock", "paper", "scissors"]

def find_winner(player, bot):
    if player==bot:
        return "Tie"
    elif (player=="rock" and bot=="scissors") or (player=="paper" and bot=="rock") or  (player=="scissors" and bot=="rock"):
         return "you win"
    else:
        return "you lose. bot victory"
    
while True:
    player_choice=input("Choose rock, paper, or scissor").lower()
    if player_choice not in player_choice:
        print("Invalid input")
        continue
    bot_choice=random.choice(choices)
    print(f"bot chooses: {bot_choice}")

    result=find_winner(player_choice, bot_choice)
    print(result)
        