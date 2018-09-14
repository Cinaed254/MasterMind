# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp pavilion 15
#
# Created:     03-09-2018
# Copyright:   (c) hp pavilion 15 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------
# !/usr/bin/python
from random import choice

number_of_players = 0
random_code=""
game_keeper={}
names=[]

FILE=open("masterMind.txt", "w", 1)
COLORS = "RGBYOP"

def random_code_generator():
    random_code_set = set()
    global random_code
    random_code=""
    while len(random_code_set) < 4:
        random_code_set.add(choice(COLORS))
    for code in random_code_set:
        random_code += code
    return (random_code)


def get_player_names():
    global names, number_of_players, game_keeper
    num=0
    while num<number_of_players:
        name = (str)(input("Enter player's name: "))
        names.append(name)
        game_keeper[name]={}
        game_keeper[name]['Score']=0
        game_keeper[name]['Won']=0
        num += 1

def name_randomizer():
    global names, number_of_players;
    random_name_set=set()
    while len(random_name_set) < number_of_players:
        random_name_set.add(choice(names))
    names=[]
    for name in random_name_set:
        names.append(name)

def guesser():
    global names, random_code, FILE
    num=0
    black_pins_taken=""
    white_pins_taken=""
    pins=""
    answer=""
    win=[]
    max_scorer=""

    random_code_generator ()
    name_randomizer()

    print("Playing in this order ",names)

    for name, info in game_keeper.items():
        for key in info:
            if key=='Score':
               game_keeper[name]['Score']=0

    while(pins!="BBBB" and answer!=random_code):
        for name in names:
            pins = ""
            prompt = name + ", make guess of 4 colors from RGBYOP: "
            answer = (input(prompt)).upper()
            before_score=game_keeper[name]['Score']
            for col in answer:
                if (random_code[answer.index(col)] == col) and (black_pins_taken.__contains__(col)==False):
                    game_keeper[name]['Score'] += 5
                    pins+="B"
                    black_pins_taken+=col
                elif(random_code[answer.index(col)] == col) and (black_pins_taken.__contains__(col)==True):
                    pins+="B"
                else:
                    for i in range(0, 4):
                        if (col is random_code[i]) and (white_pins_taken.__contains__(col)==False):
                            game_keeper[name]['Score']+=1
                            pins+="W"
                            white_pins_taken+=col
                        elif(col is random_code[i]) and (white_pins_taken.__contains__(col)==True):
                            pins+="W"

            print("Result ", pins)
            print("Current Player: ", name, "Current Score: ", before_score)
            print("Current Player: ", name, "Updated Score: ", game_keeper[name]['Score'])
            if max_scorer!="":
                if game_keeper[name]['Score'] > game_keeper[max_scorer]['Score']:
                    for name, key in game_keeper.items():
                        max_scorer=name
            else: max_scorer=name
            if answer == random_code:
                print("Correct guess!")
                game_keeper[name]['Won']+=1
                game_keeper[max_scorer]['Won']+=1

                win=name
                break
            num += 1
            print("Max Scorer: ",max_scorer)

            #clue
            print(random_code)
        num=0
    print(max_scorer)
    print(game_keeper)

    print("Winner: ",win , game_keeper[win])

    file_output_string="Results: "+(str)(game_keeper)+"\nWinner: "+win+(str)(game_keeper[win])+"\n"
    FILE.write(file_output_string)

def main():
    global score_keeper, number_of_players
    print(type(game_keeper))
    number_of_players = (int)(input("Enter number of players: "))
    get_player_names()

    cont=""
    while cont=="":
        guesser()
        print("<ENTER> to play and any letter to stop: ")
        cont=input()
        if cont=="":
            continue
        else:
            break

    most_wins=0
    for name, data in game_keeper.items():
        for key in data:
            if key=='Won':
                if data[key]>most_wins:
                    most_wins=data[key]

    winners=[]
    for nam, dat in game_keeper.items():
        if dat['Won']==most_wins:
            winners.append(name)

    for nm in winners:
        print("Overall Winner: ", nm)

    print("Program end")
    FILE.close ()

if __name__ == '__main__':
    main()
