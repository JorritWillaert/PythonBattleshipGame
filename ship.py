from box import Box

class Ship(Box):
    ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}

    def __init__(self, board, coordinates, name):
        self.sunk_coordinates = []
        self.coordinates = []
        self.initialize_coordinates(board, coordinates)
        self.change_boxes_to_ship()
        self.name = name

    def change_boxes_to_ship(self):
        """Change the boxes from '.' to '@'."""
        for box in self.coordinates:
            box.change_to_ship()

    def initialize_coordinates(self, board, coordinates):
        """Append all the box objects to a list named 'coordinates'"""
        for coordinate in coordinates:
            self.coordinates.append(board.find_coordinate(coordinate))

    def change_boxes_to_sunk(self):
        for box in self.sunk_coordinates:
            box.change_to_sunk()
