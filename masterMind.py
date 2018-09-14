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
names=[]
score_keeper=[]
game_keeper=[]

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
    global names, number_of_players
    num=0
    while num<number_of_players:
        name = input("Enter player's name: ")
        names.append(name)
        score_keeper.append(0)
        game_keeper.append(0)
        num += 1


def guesser():
    global names, random_code, score_keeper, FILE
    num=0
    black_pins_taken=""
    white_pins_taken=""
    pins=""
    answer=""
    win=[]

    random_code_generator ()

    i=0;
    for score in score_keeper:
        score_keeper[i]=0
        i+=1

    while(pins!="BBBB" and answer!=random_code):
        for name in names:
            pins = ""
            prompt = name + ", make guess of 4 colors from RGBYOP: "
            answer = (input(prompt)).upper()
            before_score=score_keeper[num]
            for col in answer:
                if (random_code[answer.index(col)] == col) and (black_pins_taken.__contains__(col)==False):
                    score_keeper[num] += 5
                    pins+="B"
                    black_pins_taken+=col
                elif(random_code[answer.index(col)] == col) and (black_pins_taken.__contains__(col)==True):
                    pins+="B"
                else:
                    for i in range(0, 4):
                        if (col is random_code[i]) and (white_pins_taken.__contains__(col)==False):
                            score_keeper[num]+=1
                            pins+="W"
                            white_pins_taken+=col
                        elif(col is random_code[i]) and (white_pins_taken.__contains__(col)==True):
                            pins+="W"

            print("Result ", pins)
            print("Current Player: ", name, "Current Score: ", before_score)
            print("Current Player: ", name, "Updated Score: ", score_keeper[num])
            if answer == random_code:
                print("Correct guess!")
                game_keeper[num]+=1
                max_score = max (score_keeper)
                game_keeper[score_keeper.index (max_score)] += 1
                win = [name, score_keeper[names.index(name)], game_keeper[names.index(name)]]
                break
            num += 1
        num=0

    results=[]
    for i in range(0, number_of_players):
        results+=[[names[i], score_keeper[i], game_keeper[i]]]
    print(results)

    print("Winner: ", win)

    file_output_string="Results: "+(str)(results[0:])+"\nWinner: "+(str)(win[0:])
    FILE.write(file_output_string)

def main():
    global score_keeper, number_of_players
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

    print("Overall Winner/s: ")
    winner_tie_count=game_keeper.count(max(game_keeper))
    for i in range(0, winner_tie_count):
        print([names[game_keeper.index(max(game_keeper))], score_keeper[game_keeper.index(max(game_keeper))], game_keeper[game_keeper.index(max(game_keeper))]])
        game_keeper[game_keeper.index(max(game_keeper))]=0

    print("Program end")
    FILE.close ()

if __name__ == '__main__':
    main()
