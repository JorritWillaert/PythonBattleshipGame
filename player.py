from board import Board
import game_functions as gf
from ship import Ship

import time
import collections

class Player():
    def __init__(self, name):
        self.warships = []
        self.name = name
        self.board_obj = Board()

    def draw_ship(self, position, direction, ship):
        """Create a new ship, draw it and append it to warships."""
        row, column = gf.convert_position(position)
        coordinates = []
        for length in range(ship[1]):
            if direction == 'h':
                coordinates.append((row, column + length))
            else:
                coordinates.append((row + length, column))
        new_ship = Ship(self.board_obj, coordinates, ship[0])
        new_ship.change_boxes_to_ship()
        self.warships.append(new_ship)

    def draw_boards(self, own, opponent):
        """Draw the board of the enemy first, then own board."""
        print("Enemy's board:")
        opponent.board_obj.print_board("enemy")
        print("Own board:")
        self.board_obj.print_board("own")

    def check_if_hit(self, coordinate):
        element = self.board_obj.find_coordinate(coordinate)
        if element.symbol == '@':
            element.symbol = 'X'
            element.is_visible = True
            for ship in self.warships:
                for coor in ship.coordinates:
                    if coor == element:
                        ship.sunk_coordinates.append(element)
            return True

        else:
            element.symbol = 'O'
            element.is_visible = True
            return False

    def check_if_sunk(self):
        for ship in self.warships:
            if collections.Counter(ship.coordinates) == collections.Counter(ship.sunk_coordinates):
                ship.change_boxes_to_sunk()
                self.warships.remove(ship)
                return ship.name
