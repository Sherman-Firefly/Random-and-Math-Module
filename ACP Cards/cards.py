import random

factions=["Spades", "Diamonds", "Clubs", "Hearts"]
ranks=["2", "3", "4", "5", "6", "7", "8", "9", "10", "Queen", "Jack", "Ace", "King"]

deck=[(rank, faction) for faction in factions for rank in ranks] 
cards=random.sample(deck,13)

print("Cards")

for card in cards:
    print(f"{card[0]} of {card[1]}")
