#!/usr/bin/python3
# coding: utf8

import game_functions as gf
from game_functions import Game
from player import Player

import pickle #For saving objects.
import sys

from colorama import init

def main():
    init()
    gf.print_options()
    while True:
        option = input("Select an option. ")
        if option == '1' or option == '2' or option == '3':
            break
        else:
            print('Enter a valid option!\n')

    if option == '1':
        player1 = Player(input("Player 1, enter your name please: "))
        player2 = Player(input("Player 2, enter your name please: "))

        #Start a game
        game = Game(player1, player2)
        game.starting_up(player1, player2)
        game.starting_up(player2, player1)

        # For making test players, uncomment these lines.
        #with open('test_players.pkl', 'wb') as output:
        #    pickle.dump(game, output, pickle.HIGHEST_PROTOCOL)

        run_switch(player1, player2, game)

    elif option == '2':
        player1 = Player(input("Player 1, enter your name please: "))
        cpu = Player("CPU", iscpu=True)

        game = Game(player1, cpu)
        game.starting_up(player1, cpu)
        game.starting_up_cpu(cpu)

        game.player1.draw_boards(player1, cpu)
        game.player2.draw_boards(cpu, player1)

        run_switch(player1, cpu, game)

    elif option == '3':
        #Import pre-initialized game.
        with open('test_players.pkl', 'rb') as infile:
            game = pickle.load(infile)

        run_switch(game.player1, game.player2, game)

def run_switch(player1, player2, game):
    switch = True
    while True:
        if switch:
            own = player1
            opponent = player2
        else:
            own = player2
            opponent = player1
        switch = not switch
        if not player2.isCPU:
            game.make_move(own, opponent)
            if opponent.warships:
                input("Switch players please! ")
        else:
            game.make_move_cpu(own, opponent)
        if not opponent.warships:
            if game.victory(own):
                main()
            else:
                sys.exit()


if __name__ == '__main__':
    main()
