from dic import result
import random





#create a list with digram as element
#access those list with indexing

player_choice=int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors."))

random_choice= random.randint(0,2)

print("Player Chose:")

# print(symbols_list[ch0osen_by_player])

print("Computer chose:")

# print(symbols_list[random_choice])

players_choice = (player_choice,random_choice)

print(result[players_choice])


