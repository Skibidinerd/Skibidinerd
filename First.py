import random
import sys
state=1
card={1:"Rock",2:"Paper",3:"Scisors"}
def game_start():
    print("  This is a game of rock paper scisors.")
    print("--------------------------------------------------------")
    
def player_choices():
        global player_choice
        player_choice=  int(input("Enter 1 for rock 2 for paper 3 for scisors or 4 to leave.\n"))
        if 0< int(player_choice) <4:
              print(f"you have chosen: {card[player_choice]}")
              
        elif player_choice==4:
            print("Goodbye, hope you enjoyed bruv. :d")
            sys.exit()
        else:
            while int(player_choice) <= 0 or int(player_choice)>=4:
                print("You haven't entered a valid value")
                player_choice=int(input("Enter 1 for rock 2 for paper 3 for scisors or 4 to leave.\n"))


while state==1:
    game_start()
    player_choices()
    bot_choice= random.randrange(1,4)

    if player_choice==bot_choice:
        print(f"Draw the robot chose: {card[bot_choice]}")
    if bot_choice-player_choice==1 or (player_choice==3 and bot_choice==2):
        print(f"You have Lost the robot chose: {card[bot_choice]}")
    else:
        print(f"You have won the bot chose: {card[bot_choice]}")
       
    state=int(input("Enter 1 if you want to play again or 0 if you want to leave\n"))
    if state !=1:
         print("Assalamu alaykum :D")
         sys.exit()



