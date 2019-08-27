import os
import time
import random

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def starting_up(self, own, opponent):
        """Initialize own board."""
        os.system('cls')
        ship_list = [("Destroyer", 2), ("Submarine", 3), ("Cruiser", 3), ('Battleship', 4), ('Carrier', 5)]

        input(own.name + ", press Enter if you're ready. ")
        for ship in reversed(ship_list):
            succesful = False
            while not succesful:
                os.system('cls')
                own.draw_boards(own, opponent)
                position = insert_position(own, ship, starting = True)
                direction = insert_direction()

                if check_if_possible(own, position, direction, ship):
                    succesful = True
                    own.draw_ship(position, direction, ship)
                else:
                    print("\nIt's not possible to place a ship here. Please chose an other location.\n")
                    time.sleep(2)
        os.system('cls')
        own.draw_boards(own, opponent)
        time.sleep(1)

    def make_move(self, own, opponent):
        succesful = False
        while not succesful:
            os.system('cls') #Best to comment this line for testing
            own.draw_boards(own, opponent)
            position = insert_position(own, ship = None, starting = False)
            coordinate = convert_position(position)
            if check_if_first_time(coordinate, opponent):
                succesful = True
            else:
                print('Please enter a non-chosen position.')
                time.sleep(1)

        os.system('cls') #Best to comment this line for testing
        if opponent.check_if_hit(coordinate):
            print('Hit!')
        else:
            print('Miss!')
        ships_name = opponent.check_if_sunk()
        if ships_name:
            print(ships_name + ' sunked!')
        time.sleep(1)
        own.draw_boards(own, opponent)
        time.sleep(1)

    def victory(self, own):
        os.system('cls')
        if own.name != 'CPU':
            print("Congratulations " + own.name + ", you've won.")
        else:
            print('Unfortunately, but the computer did beat you...')
        while True:
            new_game = input("Do you want to play a new game? (y, n) ")
            if new_game == 'y':
                return True
            elif new_game == 'n':
                return False
            else:
                print('Enter a valid option!\n')

    def starting_up_cpu(self, cpu):
        """Initialize cpu's board."""
        ship_list = [("Destroyer", 2), ("Submarine", 3), ("Cruiser", 3), ('Battleship', 4), ('Carrier', 5)]

        for ship in reversed(ship_list):
            succesful = False
            while not succesful:
                letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                letter = letters[random.randint(0, 9)]
                number = str(random.randint(1, 10))
                position = letter + number

                directions = ['h', 'v']
                direction = directions[random.randint(0,1)]

                if check_if_possible(cpu, position, direction, ship):
                    succesful = True
                    cpu.draw_ship(position, direction, ship)

    def make_move_cpu(self, cpu, opponent):
        if cpu.board_obj.hitted_not_sunk:
            coor = cpu.board_obj.hitted_not_sunk
            if len(coor) == 1:
                possibilities = [(coor[0][0] - 1, coor[0][0]), (coor[0][0] + 1, coor[0][0]), (coor[0][0], coor[0][0] - 1),
                (coor[0][0], coor[0][0] + 1)]
        else:
            succesful = False
            while not succesful:
                coordinate = (random.randint(0, 9), random.randint(0, 9)) #Already converted position.
                if check_if_first_time(coordinate, opponent):
                    succesful = True
            test1 = opponent.check_if_hit(coordinate)
            test2 = opponent.check_if_sunk()
            if test1 and not test2:
                cpu.board_obj.hitted_not_sunk.append(coordinate)
                #Work further...


def check_if_possible(player, position, direction, ship):
    """Check if it is possible to place a ship here."""
    row, column = convert_position(position)
    for length in range(ship[1]):
        if direction == 'h':
            if column + length >= 10 or player.board_obj.board[row][column + length].symbol != '.':
                return False
        else:
            if row + length >= 10 or player.board_obj.board[row + length][column].symbol != '.':
                return False
    return True

def convert_position(position):
    """Convert position to 'absolute' position! (B7 becomes (1, 6))"""
    letter = position[0]
    column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'].index(letter)
    row = int(position[1:]) - 1
    return row, column

def insert_position(player, ship, starting):
    """Insert a valid position (e.g. B2)."""
    while True:
        if starting:
            position = input(player.name +  ", where do you want to place your " + ship[0] + "(" + str(ship[1]) + ")? ")
        else:
            position = input(player.name +  ", where do you want to shoot? ")
        try:
            if (position[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) and (int(position[1:]) in range(1, 11)):
                return position
            else:
                print("Please insert a valid position.\n")
        except:
            print("Please insert a valid position.\n")

def insert_direction():
    """Insert a valid direction."""
    while True:
        direction = input("Do you want to place it horizontal or vertical? (h, v) ")
        try:
            if direction in ['h', 'v']:
                return direction
            else:
                print("Please insert a valid direction.\n")
        except:
            print("Please insert a valid direction.\n")

def check_if_first_time(coordinate, opponent):
    place = opponent.board_obj.find_coordinate(coordinate)
    if place.symbol == '@' or place.symbol == '.':
        return True
    else:
        return False

def print_options():
    print("""
Option 1: Duo player mode
Option 2: Single player mode (In progress...)
Option 3: Pre-initialized players
    """)
